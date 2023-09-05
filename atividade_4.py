


def adicionar_livro(lista_livros,livro) -> list:
  lista_livros.append(livro)
  return lista_livros

def remover_livro(lista_livros,livro)-> list:
  lista_livros.remove(livro)
  return lista_livros

def listar_livros(lista_livros):
  [print(x) for x in lista_livros]
