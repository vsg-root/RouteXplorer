class Utils:
    @staticmethod
    def gerar_load(fim: int, progresso: int, nome: str):
        porcentagem = (progresso//fim) * 100
        print(f"{porcentagem:03}% [" + "■" * (porcentagem//10) + "□" * (10 - (porcentagem//10)) + f"] - {nome}", end="\r" if porcentagem < 100 else "\n")