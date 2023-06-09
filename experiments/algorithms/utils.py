from abc import ABC, abstractmethod

class ElementoInvalido(Exception):
    pass

class TamanhoInvalido(ElementoInvalido):
    pass

class MapaInvalido(ElementoInvalido):
    pass


class InputReader:
    """Classe responsável por fazer a leitura do input e trata-lo
    """

    def ler_arquivo(self, caminho_arquivo: str) -> dict[str, tuple[int, int]]:
        def procurar_vertice(vertices: dict[str, tuple[int, int]], alvo: str) -> bool:
            for i in vertices.keys():
                if i == alvo:
                    return True
            return False

        with open(caminho_arquivo, "r") as arquivo:
            tamanho_mapa = ()
            try:
                tamanho_mapa = tuple(int(i) for i in arquivo.readline().split("x"))
                if len(tamanho_mapa) != 2:
                    raise TamanhoInvalido("Número inválido de dimensões!")
            except ValueError:
                raise TamanhoInvalido("O tamanho do mapa deve ser composto por dois inteiros!")

            vertices = {}
            encontrou_r = False
            for i in range(tamanho_mapa[0]):
                linha = arquivo.readline().split()[:tamanho_mapa[1]]
                if not linha or len(linha) < tamanho_mapa[1]:
                    raise MapaInvalido("O tamanho real do mapa não corresponde ao tamanho informado!")
                for j in range(tamanho_mapa[1]):
                    if not encontrou_r and linha[j] == 'R':
                        encontrou_r = True
                    if linha[j].isalpha() and not procurar_vertice(vertices, linha[j]):
                        vertices[linha[j]] = (i, j)
                    elif linha[j].isalpha():
                        raise MapaInvalido("Vértices duplicados!")

            if not encontrou_r:
                raise MapaInvalido("Ponto de retorno não encontrado!")

            return vertices


class DistanciaCalculator:
    """Classe para calcular as distâncias entre os vértices de um grafo
    """

    def get_distancias(self, vertices: dict[str, tuple[int, int]]) -> dict[str, dict[str, int]]:
        distancias = {}
        for i in vertices.keys():
            vertices_restantes = vertices.copy()
            vertices_restantes.pop(i)
            distancias[i] = dict((j, abs(vertices[i][0] - vertices[j][0]) + abs(vertices[i][1] - vertices[j][1]))
                                 for j in vertices_restantes.keys())
        return distancias

