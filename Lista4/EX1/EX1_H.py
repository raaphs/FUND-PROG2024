n = int(input("Digite a quantidade de números a serem lidos: "))
soma = 0

for i in range(n):
    numero = int(input("Digite um número: "))
    soma += numero
    
print("Soma dos números lidos: ",soma)