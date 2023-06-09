from abc import ABC, abstractmethod

class Algorithm(ABC):
    """Classe abstrata para encontrar o melhor percurso em um grafo
    """

    @abstractmethod
    def encontrar_melhor_caminho(self, vertices: list[str]) -> tuple[list[str], int]:
        pass