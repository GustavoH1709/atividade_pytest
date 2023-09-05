import random

def lista_numeros_aleatorios() -> list:
    numeros_aleatorios = []

    for i in range(20000):
        numeros_aleatorios.append(random.randint(-999999, 999999))

    return numeros_aleatorios