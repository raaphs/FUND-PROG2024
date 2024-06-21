#numeros para  adivisão
dividendo = int(input("Digite um número inteiro: "))
divisor = int(input('Digite outro número inteiro: '))

#realizar a divisão
if (divisor == 0):
    print("Erro: Divisão por 0 não é possível")
else:
    resultado = dividendo / divisor
    print('O resultado da divisão é',resultado)
