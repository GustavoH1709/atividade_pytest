from atividade_1 import lista_numeros_aleatorios
from atividade_2 import ordenar_lista
from utils import esta_ordenada

def test_verificar_lista_esta_em_ordem_1():
    lista_aleatoria = lista_numeros_aleatorios()
    lista_ordenada = ordenar_lista(lista_aleatoria)
  
    assert esta_ordenada(lista_ordenada) == True

def test_verificar_lista_esta_em_ordem_2():
    lista_aleatoria = lista_numeros_aleatorios()
    lista_ordenada = ordenar_lista(lista_aleatoria)
  
    assert esta_ordenada(lista_ordenada) == True


