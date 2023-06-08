from typing import Tuple, List, Dict


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
