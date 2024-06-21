#FUNÇÃO QUE VERIFICA SE UM NÚMERO É DIVISÍVEL PELO OUTRO
def divisivelPorN(num1, num2):
    if num2 == 0:
        print("Não é possível realizar a divisão com zero!!")
        return False
    return num1 % num2 == 0
#EXECUTANDO
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
resultado = divisivelPorN(num1, num2)
print(resultado)