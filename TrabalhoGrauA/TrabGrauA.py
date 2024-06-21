import random

#DEFININDO AS VARIAVEIS PARA CADA JOGADOR
posJogador1 = 0
posJogador2 = 0
filhosJogador1 = 0
filhosJogador2 = 0
dinheiroJogador1 = 0
dinheiroJogador2 = 0
jogador1Casado = False
jogador2Casado = False
jogador1Famoso = False
jogador2Famoso = False
jogador1Vivo = True
jogador2Vivo = True

#FUNÇÃO PARA RODAR A ROLETA E RETORNAR O RESULTADO DO MOVIMENTO
def rolarRoleta():
    return random.randint(1, 6)

#FUNÇÃO PARA MOVER O JOGADOR DE ACORDO COM O RESULTADO DA ROLETA
def moverJogador(posJogador):
    resultadoDado = rolarRoleta()
    posJogador += resultadoDado
    return posJogador

#FUNÇÃO PARA VERIFICAR SE UM JOGADOR ESTÁ NA CASA DE FILHOS
def verificarFilhos(posJogador):
    if posJogador == 4 or posJogador == 8 or posJogador == 12 or posJogador == 16 or posJogador == 20:
        return True
    else:
        return False

#FUNÇÃO PARA VERIFICAR SE UM JOGADOR ESTÁ NA CASA DE DINHEIRO
def verificarDinheiro(posJogador):
    if posJogador == 3 or posJogador == 6 or posJogador == 9 or posJogador == 15 or posJogador == 18:
        return True
    else:
        return False