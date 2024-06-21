#FUNÇÃO QUE VERIFICA O PRIMEIRO NOME NA ORDEM
def primeiroEmOrdemAlfabetica(nomes):
    #RETORNA OS NOMES EM ORDEM ALFABÉTICA
    nomesOrdenados = sorted(nomes)
    return nomesOrdenados[0]

def main():
    #SOLICITA PRO USUÁRIO QUE INFORME 5 NOMES
    nomes = []
    for i in range(5):
        nome = input(f"Informe o nome {i+1}: ")
        nomes.append(nome)

    primeiroNome = primeiroEmOrdemAlfabetica(nomes)
    print("O primeiro nome em ordem alfabética é:", primeiroNome)

#EXECUTANDO FUNÇÃO PRINCIPAL
main()