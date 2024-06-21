def ehPrimo(numero):
    #VERIFICA SE O NÚMERO É MENOR DO QUE 2
    if numero < 2:
        return False
    #VERFIFICA SE UM NÚMERO É DIVISÍVEL POR ALGUM NÚMERO ENTRE 2 E SUA RAIZ QUADRADA
    for i in range(2, int (numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numPrimoAteh(i):
    numerosPrimos = []
    numeroAtual = 2
    
    while len(numerosPrimos) < i:
        if ehPrimo(numeroAtual):
            numerosPrimos.append(numeroAtual)
        numeroAtual += 1
    return numerosPrimos

#CONSEGUINDO OS 10 PRIMEIROS NÚMEROS
primeiros10 = numPrimoAteh(10)

#EXUBUNDO OS RESULTADOS
print("Os 10 primeiros números primos são:",primeiros10)