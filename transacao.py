from dataclass import dataclass
from categoria import Categoria

@dataclass
class Transacao:
    descricao: str
    valor: float
    categoria: Categoria

    def exibir(self):
        print(f"DESCRIÇÃO: {self.descricao} | VALOR: {self.valor} | CATEGORIA: {sef.categoria}")