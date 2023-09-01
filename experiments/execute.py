from utils.input_reader import InputReader
from utils.Graph import Graph
from algorithms.BruteForceSearch import BruteForceSearch
from algorithms.AntColony import AntColonyOptimization


# Datas of graph
#graph = Graph(InputReader.get_vertices(InputReader.get_map_size(input()), input_function=input))
graph = InputReader.read_file(".\\experiments\\berlin52.tsp")

# Calculation of the best path and distance
#best_path, _ = BruteForceSearch.find_best_path(graph)

best_path, best_distance = AntColonyOptimization.find_best_path(graph)

print("Melhor caminho:", best_path)
print("Menor distância:", best_distance)
#path_length = len(best_path)
#for i in range(path_length):
#    print(best_path[i], end=" " if i < path_length - 1 else "\n")


