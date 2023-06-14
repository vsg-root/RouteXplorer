from utils.Graph import Graph
from utils.Utils import Utils
from typing import Callable, Optional, Sequence

class InvalidElement(ValueError):
    pass

class InvalidSize(InvalidElement):
    pass

class InvalidMap(InvalidElement):
    pass


class InputReader:
    """Class responsible for reading and handling the input."""
        
    @staticmethod
    def get_map_size(input: str, separator: Optional[str] = " ") -> tuple[int]:
        try:
            map_size = tuple(int(i) for i in input.split(separator))
            if len(map_size) != 2:
                raise InvalidSize("Invalid dimensions numbers.")
            if map_size[0] <= 0 or map_size[1] <= 0:
                raise InvalidSize("The map size must be positive.")
            return map_size
        except ValueError:
            raise InvalidSize("The map size must consist of two integers.")
    
    @staticmethod
    def get_vertices(map_size: tuple[int], map: Sequence[Sequence[str]] = None, input_function: Callable[[None], str] = None, separator: Optional[str] = " ") -> dict[str, tuple[int, int]]:
        if len(map_size) != 2:
            raise InvalidSize("Invalid dimensions numbers.")
        if map_size[0] <= 0 or map_size[1] <= 0:
            raise InvalidSize("The map size must be positive.")
        if map == None and input_function == None:
            raise ValueError("If a map is not passed directly an input function must be provided.")
        if map != None and len(map) < map_size[0]:
            raise InvalidMap("The actual size of the map does not correspond to the given size.")
        
        vertices = {}
        for i in range(map_size[0]):
            line = map[i] if map != None else input_function().split(separator)[:map_size[1]]
            if not line or len(line) < map_size[1]:
                raise InvalidMap("The actual size of the map does not correspond to the given size.")
            for j in range(map_size[1]):
                vertice = line[j].strip()
                if vertice.isalpha(): 
                    if not Utils.find(vertices.keys(), vertice):
                        vertices[vertice] = (i, j)
                    else:
                        raise InvalidMap("Duplicate vertices!")
        return vertices
        

    @staticmethod
    def read_file(file_path: str) -> dict[str, tuple[int, int]]:
        """Reads the input file and returns a dictionary of vertices with their coordinates.

        Args:
            file_path (str): The path to the input file.

        Returns:
            dict[str, tuple[int, int]]: A dictionary containing vertices as keys and their coordinates as values.
        """   

        with open(file_path, "r") as file:
            
            map_size = InputReader.get_map_size(file.readline())

            vertices = InputReader.get_vertices(map_size, input_function=file.readline)

            return Graph(vertices)
