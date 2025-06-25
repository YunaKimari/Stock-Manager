from datetime import datetime
from colorama import init, Fore, Style
init(autoreset=True)

class Item:
    def __init__(self, nome, validade=None, quantidade=1, quantidade_minima=1):
        self.nome = nome
        self.validade = validade
        self.data_insercao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data_remocao = None
        self.quantidade = quantidade
        self.quantidade_minima = quantidade_minima
        self.classificacao = self._classificar_estoque()
        
    def _classificar_estoque(self):
        if self.quantidade < self.quantidade_minima:
            return "Baixo"
        elif self.quantidade <= self.quantidade_minima * 2:
            return "Médio"
        else:
            return "Alto"
        
    def atualizar_classificacao(self):
        self.classificacao = self._classificar_estoque()
        
    def __repr__(self):
        cor = {
            "Baixo": Fore.RED,
            "Médio": Fore.YELLOW,
            "Alto": Fore.GREEN
        }.get(self.classificacao, "")
        
        return f"{self.nome} - Quantidade: {self.quantidade} - Classificação: {cor}{self.classificacao}{Style.RESET_ALL}"