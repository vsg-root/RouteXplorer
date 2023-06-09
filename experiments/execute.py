from utils.distance_calculator import DistanciaCalculator
from utils.input_reader import InputReader
from algorithms.BruteForceSearch import BruteForceSearch

# Dados do grafo
input_reader = InputReader()
vertices = input_reader.ler_arquivo(input("Insira o caminho do arquivo: ")) #./experiments/input.txt

distancia_calculator = DistanciaCalculator()
grafo = distancia_calculator.get_distancias(vertices)

# Construção das instâncias
melhor_caminho_finder = BruteForceSearch(grafo)

# Cálculo do melhor caminho e distância
vertices.pop("R")
melhor_caminho, melhor_distancia = melhor_caminho_finder.encontrar_melhor_caminho(list(vertices.keys()))

print("Melhor caminho:", melhor_caminho)
print("Distância:", melhor_distancia)
