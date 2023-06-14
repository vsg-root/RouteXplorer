from algorithms.Algorithm import Algorithm, InvalidReturnPoint
from utils.Graph import Graph
from utils.Utils import Utils
from typing import Optional


class BruteForceSearch(Algorithm):
    """Class implementing the Brute Force Search algorithm."""

    @staticmethod
    def __permutation(vertices: list[str], show_load: bool, depth: int = 0) -> list[list[str]]:
        """
        Generate all possible permutations of vertices using a recursive approach.

        Args:
            vertices (list[str]): The list of vertices to permute.
            show_load (bool): Flag indicating whether to show load progress.
            depth (int): The current depth of recursion.

        Returns:
            list[list[str]]: List of all possible permutations of vertices.
        """
        if len(vertices) == 1:
            return [vertices]
        result = []
        for i in range(len(vertices)):
            if show_load and depth == 0:
                Utils.generate_load(len(vertices), i + 1, "Generating permutations")
            current_vertice = vertices[i]
            remaining_vertices = vertices[:i] + vertices[i + 1:]
            remaining_permutations = BruteForceSearch.__permutation(remaining_vertices, show_load, depth + 1)  # Corrected method name
            for permutation in remaining_permutations:
                result.append([current_vertice] + permutation)
        return result

    @staticmethod
    def find_best_path(graph: Graph, return_point: Optional[str] = "R", show_load: bool = False, show_result: bool = False):
        """
        Find the best path in the given graph using Brute Force Search.

        Args:
            graph (Graph): The graph object.
            show_load (bool): Flag indicating whether to show load progress.
            show_result (bool): Flag indicating whether to show the result.

        Returns:
            tuple: A tuple containing the best path and its minimum distance.
        """
        vertices = graph.get_vertices()
        if not Utils.find(vertices, return_point):
            raise InvalidReturnPoint("Return point not found!")
        
        min_distance = float('inf')
        best_path = None

        
        vertices.remove(return_point)
        permutations = BruteForceSearch.__permutation(vertices, show_load)

        cont = 0
        for permutation in permutations:
            permutations.remove(permutation[::-1])

            if show_load:
                Utils.generate_load(len(permutations), cont + 1, "Checking paths")

            path = [return_point] + permutation + [return_point]
            distance = graph.cust_calculate(path)
            if distance < min_distance:
                min_distance = distance
                best_path = path[1:-1]
            cont += 1

        if show_result:
            print(f"Best path: {best_path}\nShorter distance: ({min_distance})")

        return best_path, min_distance
