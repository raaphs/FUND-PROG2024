def ehPrimo(numero):
    #VERIFICA SE O NÚMERO É MENOR DO QUE 2
    if numero < 2:
        return False
    #VERFIFICA SE UM NÚMERO É DIVISÍVEL POR ALGUM NÚMERO ENTRE 2 E SUA RAIZ QUADRADA
    for i in range(2, int (numero ** 0.5) + 1):
        if numero % i == 0:
            return False
        
    return True

def main():
    positivos = 0
    negativos = 0
    divisiveisPor2 = 0
    divisiveisPor5 = 0
    primos = 0
    totalNumeros = 0
    
    while True:
        numero = int(input("Digite um número inteiro(Digite 0 para sair): "))
        
        if numero == 0:
            break
        totalNumeros += 1
        
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        
        if numero % 2 == 0:
            divisiveisPor2 += 1
        
        if numero % 5 == 0:
            divisiveisPor5 += 1
        
        if ehPrimo(numero):
            primos += 1
            
    print("Porcentagem de números positivos:", (positivos / totalNumeros) * 100,"%")
    print("Porcentagem de números negativos:", (negativos / totalNumeros) * 100,"%")
    print("Porcentagem de números divisiveisPor2:", (divisiveisPor2 / totalNumeros) * 100,"%")
    print("Porcentagem de números divisiveisPor5:", (divisiveisPor5 / totalNumeros) * 100,"%")
    print("Porcentagem de números primos:", (primos / totalNumeros) * 100,"%")
    
main()