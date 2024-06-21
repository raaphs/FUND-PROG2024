import random

def sorteio(inicio, fim):
    return random.randint(inicio, fim)

#EXECUTANDO
inicio = 1
fim = 100
numeroSorteado = sorteio(inicio, fim)
print("O número sorteado é:",numeroSorteado)