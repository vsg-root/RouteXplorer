from utils.input_reader import InputReader
from algorithms.BruteForceSearch import BruteForceSearch

# Datas of graph
graph = InputReader.read_file(input("Enter file path: ")) #./experiments/input.txt

# Calculation of the best path and distance
best_path, best_distance = BruteForceSearch.find_best_path(graph)

print(" ".join(best_path))
