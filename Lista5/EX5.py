#FUNÇÕES DAS OPERAÇÕES
def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("ERRO! Divisão por zero")
        return None

#MENU
def exibirMenu():
    print("-_-_-_-CALCULADORA SIMPLES-_-_-_-")
    print("1) Somar")
    print("2) Subtrair")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Sair")
    
#FUNÇÃO PRINCIPAL
def main():
    while True:
        exibirMenu()
        opcao = input("Escolha uma das opções(1/2/3/4/5): ")
        
        if opcao == "5":
            print("Obrigado por usar a calculadora. Até mais!")
            break
        elif opcao in ["1", "2", "3", "4"]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == "1":
                print("Resultado da soma:", somar(num1, num2))
            elif opcao == "2":
                print("Resultado da subtração:", subtrair(num1, num2))
            elif opcao == "3":
                print("Resultado da multiplicação:", multiplicar(num1, num2))
            elif opcao == "4":
                resultadoDivisao = dividir(num1, num2)
                if resultadoDivisao is not None:
                    print("Resultado da divisão:", resultadoDivisao)
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
#EXECUTANDO
main()