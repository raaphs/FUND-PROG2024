#Par ou ímpar
num = float(input('Digite um número: '))
resto = num % 2

#condição
if (resto == 0):
    print('Número par')
else:
    print('Número ímpar')