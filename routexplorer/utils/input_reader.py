from .Graph import Graph

class InvalidElement(Exception):
    pass

class InvalidSize(InvalidElement):
    pass

class InvalidMap(InvalidElement):
    pass


class InputReader:
    """Class responsible for reading and handling the input."""

    @staticmethod
    def read_file(file_path: str) -> dict[str, tuple[int, int]]:
        """Reads the input file and returns a dictionary of vertices with their coordinates.

        Args:
            file_path (str): The path to the input file.

        Returns:
            dict[str, tuple[int, int]]: A dictionary containing vertices as keys and their coordinates as values.
        """
        def looking_vertices(vertices: dict[str, tuple[int, int]], target: str) -> bool:
            """Checks if a vertex already exists in the given dictionary.

            Args:
                vertices (dict[str, tuple[int, int]]): The dictionary of vertices.
                target (str): The vertex to check.

            Returns:
                bool: True if the vertex exists, False otherwise.
            """
            for i in vertices.keys():
                if i == target:
                    return True
            return False

        with open(file_path, "r") as file:
            map_size = ()
            try:
                map_size = tuple(int(i) for i in file.readline().split())
                if len(map_size) != 2:
                    raise InvalidSize("Invalid dimensions numbers!")
            except ValueError:
                raise InvalidSize("The map size must consist of two integers!")

            vertices = {}
            found_r = False
            for i in range(map_size[0]):
                line = file.readline().split()[:map_size[1]]
                if not line or len(line) < map_size[1]:
                    raise InvalidMap("The actual size of the map does not correspond to the stated size!")
                for j in range(map_size[1]):
                    if not found_r and line[j] == 'R':
                        found_r = True
                    if line[j].isalpha() and not looking_vertices(vertices, line[j]):
                        vertices[line[j]] = (i, j)
                    elif line[j].isalpha():
                        raise InvalidMap("Duplicate vertices!")

            if not found_r:
                raise InvalidMap("Return point not found!")

            return Graph(vertices)
