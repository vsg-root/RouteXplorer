from utils.input_reader import InputReader
from utils.Graph import Graph
from algorithms.BruteForceSearch import BruteForceSearch

# Datas of graph
graph = Graph(InputReader.get_vertices(InputReader.get_map_size(input()), input_function=input))

# Calculation of the best path and distance
best_path, _ = BruteForceSearch.find_best_path(graph)

path_length = len(best_path)
for i in range(path_length):
    print(best_path[i], end=" " if i < path_length - 1 else "\n")
