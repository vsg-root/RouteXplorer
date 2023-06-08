from utils import InputReader, MelhorCaminhoFinder

# Dados do grafo
input_reader = InputReader()
vertices = input_reader.ler_arquivo(input("Insira o camino do arquivo: ")) #./experiments/input.txt
grafo = input_reader.get_distancias(vertices)

# Construção das instâncias
melhor_caminho_finder = MelhorCaminhoFinder(grafo)

# Cálculo do melhor caminho e distância
vertices.pop("R")
melhor_caminho, melhor_distancia = melhor_caminho_finder.encontrar_melhor_caminho(list(vertices.keys()))

print("Melhor caminho:", melhor_caminho)
print("Distância:", melhor_distancia)
