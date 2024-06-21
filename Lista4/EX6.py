import random

#FUNÇÃO QUE CALCULA A MÉDIA DE UM LISTA DE NÚMEROS
def calcularMedia(valores):
    return sum(valores) / len(valores) if len(valores) > 0 else 0

#SORTEANDO OS 5 VALORES ENTRE 0 E 100
valoresSorteados = [random.randint(0, 100) for _ in range(5)]

menorValor = min(valoresSorteados)
maiorValor = max(valoresSorteados)

mediaValores = calcularMedia(valoresSorteados)

#EXECUTANDO
print("Valores sorteados:", valoresSorteados)
print("Menor valor:", menorValor)
print("Maior valor:", maiorValor)
print("Média dos valores:", mediaValores)