from algorithms.Algorithm import Algorithm
from utils.Grafo import Grafo
from utils.Utils import Utils


class BruteForceSearch(Algorithm):
    
    @staticmethod
    def __permutation(vertices: list[str], exibir_load: bool, profundidade: int = 0) -> list[list[str]]:
        if len(vertices) == 1:
            return [vertices]
        resultado = []
        for i in range(len(vertices)):
            if exibir_load and profundidade == 0:
                Utils.gerar_load(len(vertices), i + 1, "gerando permutações")
            vertice_atual = vertices[i]
            vertices_restantes = vertices[:i] + vertices[i + 1:]
            permutacoes_restantes = BruteForceSearch.__permutation(vertices_restantes, exibir_load, profundidade + 1)  # Corrected method name
            for permutacao in permutacoes_restantes:
                resultado.append([vertice_atual] + permutacao)
        return resultado
    
    @staticmethod
    def encontrar_melhor_caminho(grafo: Grafo, exibir_load: bool = False, exibir_resultado: bool = False):
        menor_distancia = float('inf')
        melhor_caminho = None
    
        permutacoes = BruteForceSearch.__permutation(grafo.get_vertices(), exibir_load)
        
        cont = 0
        for permutacao in permutacoes:
            permutacoes.remove(permutacao[::-1]) # Verificar se é permitido!!!
            
            if exibir_load:
                Utils.gerar_load(len(permutacoes), cont + 1, "verificando caminhos")
                
            caminho = ['R'] + permutacao + ['R']
            distancia = grafo.calcular_custo(caminho)
            if distancia < menor_distancia:
                menor_distancia = distancia
                melhor_caminho = caminho[1:-1]
            cont += 1
        
        if exibir_resultado:
            print(f"{melhor_caminho} ({menor_distancia})")

        return melhor_caminho, menor_distancia
