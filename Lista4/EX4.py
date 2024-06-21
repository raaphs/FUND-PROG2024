def numerosDivisiveis():
    divisor = int(input("Entre com o valor do divisor: "))
    inicioIntervalo = int(input("Início do intervalo: "))
    finalIntervalo = int(input("Final do intervalo: "))

    print(f"Números divisíveis por {divisor} no intervalo de {inicioIntervalo} a {finalIntervalo}:")
    for numero in range(inicioIntervalo, finalIntervalo + 1):
        if numero % divisor == 0:
            print(numero, end=" ")

#EXECUTANDO FUNÇÃO
numerosDivisiveis()