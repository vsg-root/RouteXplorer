from utils.input_reader import InputReader
from algorithms.BruteForceSearch import BruteForceSearch

# Dados do grafo
grafo = InputReader.ler_arquivo(input("Insira o caminho do arquivo: ")) #./experiments/input.txt

# Cálculo do melhor caminho e distância
melhor_caminho, melhor_distancia = BruteForceSearch.encontrar_melhor_caminho(grafo)

print(" ".join(melhor_caminho))
