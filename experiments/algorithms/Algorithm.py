from abc import ABC, abstractmethod
from utils.Grafo import Grafo

class Algorithm(ABC):
    """Classe abstrata para encontrar o melhor percurso em um grafo
    """

    @staticmethod
    @abstractmethod
    def encontrar_melhor_caminho(grafo: Grafo, exibir_load: bool = False, exibir_resultado: bool = False) -> tuple[list[str], int]:
        pass