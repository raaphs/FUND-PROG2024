####################FUNÇÕES######################
def ehPrimo(numero):
    #VERIFICA SE O NÚMERO É MENOR DO QUE 2
    if numero < 2:
        return False
    #VERFIFICA SE UM NÚMERO É DIVISÍVEL POR ALGUM NÚMERO ENTRE 2 E SUA RAIZ QUADRADA
    for i in range(2, int (numero ** 0.5) + 1):
        if numero % i == 0:
            return False
        
    return True
####################PROGRAMA#####################
numero = int(input("Digite um número inteiro para verificar se ele é primo: "))
resultado = ehPrimo(numero)
print("O número",numero,"é primo?",resultado)