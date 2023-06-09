class DistanciaCalculator:
    """Classe para calcular as distâncias entre os vértices de um grafo
    """

    def get_distancias(self, vertices: dict[str, tuple[int, int]]) -> dict[str, dict[str, int]]:
        distancias = {}
        for i in vertices.keys():
            vertices_restantes = vertices.copy()
            vertices_restantes.pop(i)
            distancias[i] = dict((j, abs(vertices[i][0] - vertices[j][0]) + abs(vertices[i][1] - vertices[j][1]))
                                 for j in vertices_restantes.keys())
        return distancias