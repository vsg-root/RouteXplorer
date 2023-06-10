class Grafo:

    Vertices = dict[str, tuple[int, int]]

    def __init__(self, vertices: Vertices) -> None:
        self.__grafo = self.__gerar_grafo(vertices)
        
    def __gerar_grafo(self, vertices: Vertices) -> dict[str, dict[str, int]]:
        distancias = {}
        for i in vertices.keys():
            vertices_restantes = vertices.copy()
            vertices_restantes.pop(i)
            distancias[i] = dict((j, abs(vertices[i][0] - vertices[j][0]) + abs(vertices[i][1] - vertices[j][1]))
                                 for j in vertices_restantes.keys())
        return distancias
    
    def get_vertices(self):
        vertice_list = list(self.__grafo.keys())
        vertice_list.remove("R")
        return vertice_list
    
    def get_distancia(self, origem: str, destino: str):
        return self.__grafo[origem][destino]
    
    def calcular_custo(self, rota):
        distancia_total = 0
        for i in range(len(rota) - 1):
            vertice_atual = rota[i]
            proximo_vertice = rota[i + 1]
            distancia_total += self.get_distancia(vertice_atual, proximo_vertice)
        return distancia_total