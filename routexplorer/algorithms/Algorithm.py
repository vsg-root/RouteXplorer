from abc import ABC, abstractmethod
from ..utils.Graph import Graph

class Algorithm(ABC):
    """
    Abstract class for finding the best path in a graph.
    """

    @staticmethod
    @abstractmethod
    def find_best_path(graph: Graph, show_load: bool = False, show_results: bool = False) -> tuple[list[str], int]:
        """
        Abstract method for finding the best path in a graph.

        Args:
            graph (Graph): The graph in which the path will be found.
            show_load (bool, optional): Flag to display loading information. Default is False.
            show_results (bool, optional): Flag to display the result of the found path. Default is False.

        Returns:
            tuple[list[str], int]: A tuple containing the best path as a list of strings and the total cost of the path as an integer.
        """
        pass
