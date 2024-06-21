import random

#DEFININDO AS PROBABILIDADES DE OBTENÇÃO DE CADA ITEM
probabilidadeComum = 0.8
probabilidadeRaro = 0.19
probabilidadeLendario = 0.01

# Variáveis para contabilizar os itens coletados
itensComuns = 0
itensRaros = 0
itensLendarios = 0

def abrirCaixa():
    global itensComuns, itensRaros, itensLendarios
    #GERA UM NÚMERO ALEATÓRIO ENTRE 0 E 1
    resultado = random.random()
    
    if resultado < probabilidadeComum:
        itensComuns += 1
        print("Você coletou 1 item comum!")
    elif resultado < probabilidadeComum + probabilidadeRaro:
        itensRaros += 1
        print("Você coletou 1 item raro!")
    else:
        itensLendarios += 1
        print("Você coletou 1 item lendário!")

def consultarItens():
    print("Itens comuns:", itensComuns)
    print("Itens raros:", itensRaros)
    print("Itens lendários:", itensLendarios)

def exibirMenu():
    print("1 - Abrir uma caixa")
    print("2 - Consultar itens")
    print("0 - Sair")

def main():
    while True:
        exibirMenu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Obrigado por usar o sistema de lootbox. Até mais!")
            break
        elif opcao == "1":
            abrirCaixa()
        elif opcao == "2":
            consultarItens()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
#EXECUTANDO
main()