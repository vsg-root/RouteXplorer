from utils import Grafo, CalculadorDistancia, MelhorCaminhoFinder

# Dados do grafo
arestas = {
    'R': {'A': 3, 'B': 2, 'C': 5, 'D': 7},
    'A': {'R': 3, 'B': 3, 'C': 4, 'D': 4},
    'B': {'R': 2, 'A': 3, 'C': 3, 'D': 5},
    'C': {'R': 5, 'A': 4, 'B': 3, 'D': 2},
    'D': {'R': 7, 'A': 4, 'B': 5, 'C': 2}
}

# Construção das instâncias
grafo = Grafo(arestas)
calculador_distancia = CalculadorDistancia(grafo)
melhor_caminho_finder = MelhorCaminhoFinder(grafo, calculador_distancia)

# Cálculo do melhor caminho e distância
vertices = ['A', 'B', 'C', 'D']

melhor_caminho, melhor_distancia = melhor_caminho_finder.encontrar_melhor_caminho(vertices)

print("Melhor caminho:", melhor_caminho)
print("Distância:", melhor_distancia)
