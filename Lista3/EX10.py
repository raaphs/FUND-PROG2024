import random

#SIMULAR AS FACES
def simular_dados(num_faces):
    if num_faces not in [4, 6, 8, 10, 12, 16]:
        print("Número de faces inálido!")
        return
    #RESULTADO
    resultado = random.randint(1, num_faces)
    print("O resultado do dado de",num_faces,"faces é: ",resultado)

#SIMULANDO O DADO
num_faces = int(input("Digite o número de faces do dado (4, 6, 8, 10, 12, 16): "))
simular_dados(num_faces)