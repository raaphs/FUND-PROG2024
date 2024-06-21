#FUNÇÃO QUE VERIFICA SE UM NÚMERO É DIVISÍVEL POR 2
def divisivelPor2(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
#EXECUTANDO
numero = int(input("Digite um número inteiro: "))
resultado = divisivelPor2(numero)
print(resultado)