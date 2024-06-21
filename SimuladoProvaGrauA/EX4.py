import random
#FUNÇÃO DE SORTEIO
def sorteio():
    numerosSorteados = random.randint(1,10)
    tentativas = 3
    
    print("Bem-Vindo ao Jogo da Adivinhação")
    print("Tente adivinhar o número de 1 a 10. Você possui 3 tentativas")
    
    #RANGE DENTRO DAS TENTATIVAS    
    for i in range(tentativas):
        palpite = int(input("Digite seu palpite:"))
        
        if palpite == numerosSorteados:
            print("Parabéns!! Você acertou o número!!")
            break
        else:
            print("Você errou o número. Tente novamente!")
    else:
        print("Suas tentativas se esgotaram. O número sorteado era: ",numerosSorteados)
sorteio()