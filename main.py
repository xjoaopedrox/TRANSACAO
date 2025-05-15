from categoria import Categoria
from transacao import Transacao


c = Categoria(nome="Receitas")
  
print(c.nome)

t1 = Transacao(
    descricao="Salario Mai/2025",
    valor = 1000.0,
    categoria=c
    )

t1.exibir()



