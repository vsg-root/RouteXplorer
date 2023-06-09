from abc import ABC, abstractmethod


class Algorithm(ABC):
    """Classe abstrata para encontrar o melhor percurso em um grafo
    """

    @abstractmethod
    def encontrar_melhor_caminho(self, vertices: list[str]) -> tuple[list[str], int]:
        pass

class BruteForceSearch(Algorithm):
    def __init__(self, grafo):
        self.grafo = grafo

    def calcular_distancia(self, caminho):
        distancia_total = 0
        for i in range(len(caminho) - 1):
            vertice_atual = caminho[i]
            proximo_vertice = caminho[i + 1]
            distancia_total += self.grafo[vertice_atual][proximo_vertice]
        return distancia_total

    def permutacoes(self, vertices):
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

    def encontrar_melhor_caminho(self, vertices):
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
