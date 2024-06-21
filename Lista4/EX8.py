#FUNÇÃO QUE CALCULA O FATORIAL
def calcularFatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, numero + 1):
            fatorial *= i
        return fatorial
#FUNÇÃO PRINCIPAL
def main():
    while True:
        numero = int(input("Entre com um número: "))
        fatorial = calcularFatorial(numero)
        print(f"O fatorial de {numero} é {fatorial}")
        continuar = input("Calcular outro número (s/n)? ").lower()
        #PROGRAMA PARA QUANDO RETORNA NÃO
        if continuar != 's':
            break
#EXECUTANDO FUNÇÃO PRINCIPAL
main()