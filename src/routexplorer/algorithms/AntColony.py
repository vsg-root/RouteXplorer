from algorithms.Algorithm import Algorithm, InvalidReturnPoint
from utils.Graph import Graph
from utils.Utils import Utils
from typing import List, Dict, Optional

import random

class AntColonyOptimization(Algorithm):
    """Class implementing the Ant Colony Optimization algorithm."""
    
    @staticmethod
    def __traverse_graph(graph: Graph, source_node: int, pheromone_matrix: Dict[str, Dict[str, int]], distance_matrix: Dict[str, Dict[str, int]], alpha: int, beta: int) -> (List[int], float):
        vertices = graph.get_vertices()
        n_nodes = len(vertices)
        
        visited = [False] * n_nodes
        visited[source_node] = True

        cycle = [source_node] * (n_nodes + 1)
        steps = 0
        current = source_node
        total_length = 0
        
        while steps < n_nodes -1:
            idx = 0
            jumps_neighbors = [0] * (n_nodes - steps)
            jumps_values = [0] * (n_nodes - steps)
            for node in range(n_nodes):
                if not visited[node]:
                    pheromone_level  = Utils.get_largest(pheromone_matrix[vertices[current]][vertices[node]], 1e-5)
                    distance_level  = Utils.get_largest(distance_matrix[vertices[current]][vertices[node]], 1e-5)
                    value = (pheromone_level**alpha ) * (distance_level**beta)
                    jumps_neighbors[idx] = node
                    jumps_values[idx] = value
                    idx += 1
            
            next_node = random.choices(jumps_neighbors, weights = jumps_values)[0]
            
            visited[next_node] = True
            
            current = next_node
            cycle[steps + 1] = current
            steps+=1

        #print([vertices[i] for i in cycle])
        total_length = graph.cust_calculate([vertices[i] for i in cycle]) 
        return cycle[:-1], total_length
    
    @staticmethod
    def __reinforcement(graph: Graph, route, value, pheromone_matrix):
        vertices = graph.get_vertices()
        if graph.get_distance(vertices[route[0]], vertices[route[1]]) < graph.get_distance(vertices[route[-1]], vertices[route[0]]):
            for i in range(1, len(route)):
                pheromone_matrix[vertices[route[i - 1]]][vertices[route[i]]] += value
            pheromone_matrix[vertices[route[-1]]][vertices[route[0]]] += value
        else:
            for i in range(1, len(route)):
                pheromone_matrix[vertices[route[i]]][vertices[route[i - 1]]] += value
            pheromone_matrix[vertices[route[0]]][vertices[route[-1]]] += value
    
    
    @staticmethod
    def find_best_path(
        graph: Graph, 
        return_point: Optional[str] = "1", 
        num_ants: Optional[int] = 146, 
        num_iterations: Optional[int] = 321,
        pheromone_initial: Optional[float] = 0.0001,
        evaporation_rate: Optional[float] = 0.3,
        alpha: Optional[float] = 0.5,
        beta: Optional[float] = 2.9,
        k: Optional[int] = 1, 
        Q: Optional[float] = 0.4,
        update_by="quality", 
        worst=False, 
        elitist=False,
        show_load: Optional[bool] = False, 
        show_result: Optional[bool] = False):
        
        vertices = graph.get_vertices()
        if not Utils.find(vertices, return_point):
            raise InvalidReturnPoint("Return point not found!")
        source_node_idx = 0
        
        distance_matrix = {}
        pheromone_matrix = {}
        for i in range(len(vertices)):
            pheromone_matrix[vertices[i]] = {}
            distance_matrix[vertices[i]] = {}
            for j in vertices:
                if j != vertices[i]:
                    pheromone_matrix[vertices[i]][j] = pheromone_initial
                    distance_matrix[vertices[i]][j] = 1/graph.get_distance(vertices[i], j) if graph.get_distance(vertices[i], j) != 0 else 0
            if vertices[i] == return_point:
                source_node_idx = i
        best_route = None
        best_cost = float('inf')

        for i in range(num_iterations):
            # trail_aux.fill(0)
            batch = [([], 0)] * num_ants
            for f in range(num_ants):
                trail = AntColonyOptimization.__traverse_graph(graph, source_node_idx, pheromone_matrix, distance_matrix, alpha, beta)
                if show_load:
                    Utils.generate_load(num_ants, f + 1, f'Round: {i + 1} \tLast Ant: {trail[1]} \t Best: {best_cost}')
                batch[f] = trail
                if trail[1] < best_cost:
                    best_cost = trail[1]
                    best_route = trail[0]
            
            # evaporação
            for j in pheromone_matrix.keys():
                for l in pheromone_matrix[j].keys():
                    pheromone_matrix[j][l] *=  1 - evaporation_rate

            for j in range(num_ants):
                delta = Q/batch[j][1]
                for l in range(len(batch[j][0]) - 1):
                    start = vertices[batch[j][0][l]]
                    end = vertices[batch[j][0][l + 1]]
                    pheromone_matrix[start][end] += delta
                pheromone_matrix[vertices[batch[j][0][-1]]][vertices[batch[j][0][0]]] += delta

            
            Utils.heap_sort(batch, num_ants, lambda x: x[1])    
            # reforço
            if worst:
                solution = batch[-1][0]
                AntColonyOptimization.__reinforcement(graph, solution, -1, pheromone_matrix)

            if elitist:
                AntColonyOptimization.__reinforcement(graph, best_route, 1, pheromone_matrix)

            if update_by == 'quality':
                for solution, _ in batch[:k]:
                    AntColonyOptimization.__reinforcement(graph, solution, 1, pheromone_matrix)
            elif update_by == 'rank':
                delta = k
                for solution, _ in batch[:k]:
                    AntColonyOptimization.__reinforcement(graph, solution, delta, pheromone_matrix)
                    delta -= 1
        
        translated_best_route = [vertices[best_route[i]] for i in range(1, len(best_route))]
        if show_result:
            print(f"Best path: {translated_best_route}\nShorter distance: ({best_cost})")
        return translated_best_route, best_cost
