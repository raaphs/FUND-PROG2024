import random

def gerarToupeiras():
    matriz = [['-' for _ in range(4)] for _ in range(4)]
    toupeirasPos = set()
    
    while len(toupeirasPos) < 4:
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        if (i, j) not in toupeirasPos:
            toupeirasPos.add((i, j))
            matriz[i][j] = 'T'
    
    return matriz

def imprimirMatriz(matriz, geracao):
    print(f"Geração {geracao}:")
    for linha in matriz:
        print(" ".join(linha))
    print()

#GERA E IMPRIMI AS TRÊS GERAÇÕES DAS MATRIZES
for geracao in range(1, 4):
    matriz = gerarToupeiras()
    imprimirMatriz(matriz, geracao)