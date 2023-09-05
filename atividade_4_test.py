from atividade_4 import adicionar_livro,listar_livros,remover_livro

def test_adicionar_livro():
  lista_livros = []
  lista_livros = adicionar_livro(listar_livros,"The Witcher")
  
  assert len(lista_livros) > 0

def test_remover_livro():
  lista_livros = []
  lista_livros = adicionar_livro(listar_livros,"The Witcher")
  lista_livros = remover_livro(listar_livros,"The Witcher")

  assert len(lista_livros) == 0

def test_listar_livros():
  lista_livros = []
  lista_livros = adicionar_livro(listar_livros,"The Witcher")
  lista_livros = adicionar_livro(listar_livros,"Livro B")
  lista_livros = adicionar_livro(listar_livros,"Livro C")

  listar_livros(lista_livros)
  
  assert len(lista_livros) == 3