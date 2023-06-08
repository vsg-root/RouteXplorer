
class ElementoInvalido(Exception):
    pass
class TamanhoInvalido(ElementoInvalido):
    pass
class MapaInvalido(ElementoInvalido):
    pass


class MelhorCaminhoFinder:
    """Classe responsável por achar o melhor percurso em um grafo
    """
    def __init__(self, grafo: dict[str, dict[str, int]]):
        """Método __init__

        Args:
            grafo (dict[str, dict[str, int]]): Grafo a ser analizado.
        """
        self.grafo = grafo
        
    def calcular_distancia(self, caminho: list[str]) -> int:
        """Calcula a distância de um determinado caminho

        Args:
            caminho (list[str]): lista dos vértices que compõem o caminho

        Returns:
            int: distância total do caminho
        """
        distancia_total = 0
        for i in range(len(caminho) - 1):
            vertice_atual = caminho[i]
            proximo_vertice = caminho[i + 1]
            distancia_total += self.grafo[vertice_atual][proximo_vertice]
        return distancia_total
    
    def permutacoes(self, vertices: list[str]) -> list[list[str]]:
        """Gera todas as permutações possíveis de um determinado grupo de vértices.

        Args:
            vertices (list[str]): Lista de vértices.

        Returns:
            list[list[str]]: lista de permutações.
        """
        if len(vertices) == 1:
            return [vertices]
        resultado = []
        for i in range(len(vertices)):
            vertice_atual = vertices[i]
            vertices_restantes = vertices[:i] + vertices[i + 1:]
            permutacoes_restantes = self.permutacoes(vertices_restantes)
            for permutacao in permutacoes_restantes:
                resultado.append([vertice_atual] + permutacao)
        return resultado

    def encontrar_melhor_caminho(self, vertices: list[str]) -> tuple[list[str], int]:
        menor_distancia = float('inf')
        melhor_caminho = None

        permutacoes = self.permutacoes(vertices)
        for permutacao in permutacoes:
            permutacoes.remove(permutacao[::-1]) # Verificar se é permitido!!!
            caminho = ['R'] + permutacao + ['R']
            distancia = self.calcular_distancia(caminho)
            if distancia < menor_distancia:
                menor_distancia = distancia
                melhor_caminho = caminho

        return melhor_caminho, menor_distancia

class InputReader():
    """Classe responsável por fazer a leitura do input e trata-lo
    """
    def ler_arquivo(self, caminho_arquivo: str) -> dict[str, tuple[int, int]]:
        """Lê o arquivo de input passado como parâmetro.

        Args:
            caminho_arquivo (str): Caminho do arquivo.

        Returns:
            dict[str, tuple[int, int]]: Dicíonário com todos os vértices e as suas respectivas coordenadas.
        """
      
        def procurar_vertice(vertices: dict[str, tuple[int, int]], alvo: str) -> bool:
            """Verifica se um vértice esta no dicionário de vértices passado como parâmetro.

            Args:
                vertices (dict[str, tuple[int, int]]): Dicionário com todos os vértices e as suas respectivas coordenadas.
                alvo (str): vértice alvo da busca

            Returns:
                bool: resultado da busca.
            """
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
            
            if not encontrou_r :
                raise MapaInvalido("Ponto de retorno não encontrado!")
            
            return vertices
                
    def get_distancias(self, vertices: dict[str, tuple[int, int]]) -> dict[str, dict[str, int]]:
        """Calcula a distâcia de cada vertice para todos os outros.

        Args:
            vertices (dict[str, tuple[int, int]]): Dicionário com todos os vértices e as suas respectivas coordenadas.

        Returns:
            dict[str, dict[str, int]]: Dicionário com a distância de cada vertice para todos os demais.
        """
        distancias = {}
        for i in vertices.keys():
            vertices_restantes = vertices.copy()
            vertices_restantes.pop(i)
            distancias[i] = dict((j, abs(vertices[i][0] - vertices[j][0]) + abs(vertices[i][1] - vertices[j][1])) for j in vertices_restantes.keys())
        return distancias
