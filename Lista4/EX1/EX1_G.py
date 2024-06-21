import random
positivos = 0
negativos = 0

for i in range(20):
    numero = random.randint(-10,10)
    if numero > 0:
        print(numero, "POSITIVO")
        positivos += 1
    elif numero < 0:
        print(numero, "NEGATIVO")
        negativos += 1
    else:
        print(numero, "NULO")
        
print("Quantidade de números positivos: ",positivos)
print("Quantidade de números negativos: ",negativos)
