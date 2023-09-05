from atividade_1 import lista_numeros_aleatorios

def test_lista_numeros_aleatorios_1():
    assert len(lista_numeros_aleatorios()) == 20000

def test_lista_numeros_aleatorios_2():
    assert all(x < 1_000_000 or x > -1_000_000 for x in lista_numeros_aleatorios())
