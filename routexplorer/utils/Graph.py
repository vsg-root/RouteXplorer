class Graph:
    """
    Class representing a graph.

    Attributes:
        Vertices (dict[str, tuple[int, int]]): Type hint for the vertices dictionary.

    Methods:
        __init__(self, vertices: Vertices) -> None:
            Initializes the Graph object.

        __generate_graph(self, vertices: Vertices) -> dict[str, dict[str, int]]:
            Generates the graph by calculating distances between vertices.

        get_vertices(self):
            Returns a list of vertices in the graph.

        get_distance(self, origin: str, destiny: str):
            Returns the distance between two vertices.

        cust_calculate(self, rota):
            Calculates the total distance of a given route.
    """

    Vertices = dict[str, tuple[int, int]]

    def __init__(self, vertices: Vertices) -> None:
        """
        Initializes the Graph object.

        Args:
            vertices (Vertices): The dictionary of vertices with their coordinates.
        """
        self.__graph = self.__generate_graph(vertices)

    def __generate_graph(self, vertices: Vertices) -> dict[str, dict[str, int]]:
        """
        Generates the graph by calculating distances between vertices.

        Args:
            vertices (Vertices): The dictionary of vertices with their coordinates.

        Returns:
            dict[str, dict[str, int]]: The graph represented as a dictionary of distances between vertices.
        """
        distances = {}
        for i in vertices.keys():
            remaining_vertices = vertices.copy()
            remaining_vertices.pop(i)
            distances[i] = dict(
                (j, abs(vertices[i][0] - vertices[j][0]) + abs(vertices[i][1] - vertices[j][1]))
                for j in remaining_vertices.keys()
            )
        return distances

    def get_vertices(self):
        """
        Returns a list of vertices in the graph.

        Returns:
            list: A list of vertices.
        """
        vertice_list = list(self.__graph.keys())
        vertice_list.remove("R")
        return vertice_list

    def get_distance(self, origin: str, destiny: str):
        """
        Returns the distance between two vertices.

        Args:
            origin (str): The starting vertex.
            destiny (str): The ending vertex.

        Returns:
            int: The distance between the two vertices.
        """
        return self.__graph[origin][destiny]

    def cust_calculate(self, rota):
        """
        Calculates the total distance of a given route.

        Args:
            rota (list): The route represented as a list of vertices.

        Returns:
            int: The total distance of the route.
        """
        total_distance = 0
        for i in range(len(rota) - 1):
            current_vertice = rota[i]
            next_vertice = rota[i + 1]
            total_distance += self.get_distance(current_vertice, next_vertice)
        return total_distance
