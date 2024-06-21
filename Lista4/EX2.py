import random
#FUNÇÂO DE ADIVINHAR O NÚMERO
def adivinharNumero():
    numeroSecreto = random.randint(1, 10)
    tentativas = 3

    print("Tente adivinhar um número de 1 a 10!")
    while tentativas > 0:
        tentativa = int(input("Tentativa {}: ".format(4 - tentativas)))
        
        if tentativa == numeroSecreto:
            print("Parabéns! Você acertou o número {}!".format(numeroSecreto))
            return  #SAI DA FUNÇÃO DEPOIS DE ACERTAR O NÚMERO
        elif tentativa < numeroSecreto:
            print("O número a adivinhar está acima de {}.".format(tentativa))
        else:
            print("O número a adivinhar está abaixo de {}.".format(tentativa))
        
        tentativas -= 1
    
    print("Suas tentativas acabaram! O número correto era {}.".format(numeroSecreto))

#EXECUTANDO A FUNÇÃO
adivinharNumero()