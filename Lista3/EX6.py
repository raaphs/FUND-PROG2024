import random
#Escolhendo PAR ou ÍMPAR
escolha_usuario = input("Você escolhe PAR ou ÍMPAR? ").upper()
while escolha_usuario not in ['PAR', 'ÍMPAR']:
    escolha_usuario = input("Escolha inválida. Você escolhe PAR ou ÍMPAR? ").upper()

#Escolhendo os números
numero_usuario = int(input("Digite um número de 0 a 5: "))
while numero_usuario < 0 or numero_usuario > 5:
    numero_usuario = int(input("Número inválido. Digite um número de 0 a 5: "))

numero_pc = random.randint(0, 5)

print("O número sorteado pelo pc foi:",numero_pc)

#SOMA
soma = numero_usuario + numero_pc
resultado = "PAR" if soma % 2 == 0 else "ÍMPAR"

#RESULTADO DO JOGO
if escolha_usuario == resultado:
    print("Você venceu!!")
else:
    print("O programa venceu!")