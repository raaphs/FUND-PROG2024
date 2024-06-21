#FUNÇÃO DE RETORNAR O PADRÃO
def imprimirPadrao(n, caracter):
    for i in range(1, n + 1):
        print(caracter * i)

#SOLICITA AO USUÁRIO O NUMERO DE LINHAS E CARACTER
numeroLinhas = int(input("Entre com um número de linhas: "))
caractere = input("Entre com um caracter: ")

#EXECUTANDO A FUNÇÃO
imprimirPadrao(numeroLinhas, caractere)