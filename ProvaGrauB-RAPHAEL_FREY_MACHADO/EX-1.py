import random

def shuffleArray(lista):
    n = len(lista)
    for _ in range(n):
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        lista[i], lista[j] = lista[j], lista[i]
    return lista

#EMBARALHANDO O ARRAY CRIADO

array = ['A', 'B', 'C', 'D', 'E']
print("Array inicial:", array)
arrayEmbaralhado = shuffleArray(array)
print("Array embaralhado:", arrayEmbaralhado)