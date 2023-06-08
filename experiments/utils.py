from typing import Tuple, List, Dict


class ElementoInvalido(Exception):
    pass
class TamanhoInvalido(InvalidElement):
    pass
class MapaInvalido(InvalidElement):
    pass

class Grafo:
    def __init__(self, arestas: Dict[str, Dict[str, int]]):
        self.grafo = self.construir_grafo(arestas)

    def construir_grafo(self, arestas: Dict[str, Dict[str, int]]) -> Dict[str, Dict[str, int]]:
        grafo = {}
        for origem, destinos in arestas.items():
            grafo[origem] = {}
            for destino, peso in destinos.items():
                grafo[origem][destino] = peso
        return grafo

    def obter_peso(self, origem: str, destino: str) -> int:
        return self.grafo[origem][destino]


class CalculadorDistancia:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo

    def calcular_distancia(self, caminho: List[str]) -> int:
        distancia_total = 0
        for i in range(len(caminho) - 1):
            vertice_atual = caminho[i]
            proximo_vertice = caminho[i + 1]
            distancia_total += self.grafo.obter_peso(vertice_atual, proximo_vertice)
        return distancia_total


class MelhorCaminhoFinder:
    def __init__(self, grafo: Grafo, calculador_distancia: CalculadorDistancia):
        self.grafo = grafo
        self.calculador_distancia = calculador_distancia

    def permutacoes(self, vertices: List[str]) -> List[List[str]]:
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

    def encontrar_melhor_caminho(self, vertices: List[str]) -> Tuple[List[str], int]:
        menor_distancia = float('inf')
        melhor_caminho = None

        permutacoes = self.permutacoes(vertices)
        for permutacao in permutacoes:
            caminho = ['R'] + permutacao + ['R']
            distancia = self.calculador_distancia.calcular_distancia(caminho)
            if distancia < menor_distancia:
                menor_distancia = distancia
                melhor_caminho = caminho

        return melhor_caminho, menor_distancia

class InputReader():
    """Classe responsável por fazer a leitura do input e trata-lo"""
   
    def ler_arquivo(self, caminho_arquivo: str) -> dict:
        """Lê o arquivo de input passado como parâmetro.

        Args:
            caminho_arquivo (str): Caminho do arquivo.

        Returns:
            dict: Dicíonário com as coordenadas de cada vértice.
        """
      
        def procurar(vertices: dict, alvo: str) -> bool:
            """Verifica se um vértice esta no dicionário de vértices passado como parâmetro.

            Args:
                vertices (dict): Dicionário com todos os vértices.
                alvo (str): vértice alvo da busca.

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
                    if linha[j].isalpha() and not procurar(vertices, linha[j]):
                        vertices[linha[j]] = (i, j)
                    elif linha[j].isalpha():
                      raise MapaInvalido("Vértices duplicados!")
            
            if not encontrou_r :
                raise MapaInvalido("Ponto de retorno não encontrado!")
            
            return vertices
                
    def get_distancias(self, vertices: dict) -> dict:
        """Calcula a distâcia de cada vertice para todos os outros.

        Args:
            vertices (dict): Dicionário com todos os vértices.

        Returns:
            dict: Dicionário com a distância de cada vertice para todos os demais.
        """
        distancias = {}
        for i in vertices.keys():
            vertices_restantes = vertices.copy()
            vertices_restantes.pop(i)
            distancias[i] = dict((j, abs(vertices[i][0] - vertices[j][0]) + abs(vertices[i][1] - vertices[j][1])) for j in vertices_restantes.keys())
        return distancias
