#FUNÇÃO PARA CALCULAR A NOVA MÉDIA
def calcularMedia(notaA, notaB, notaC, substituir):
    if substituir.upper() == 'A':
        #NÂO SEI SE É A MESMA CONTA PARA FAZER A NOVA MÉDIA :(
        novaMedia = (notaB + notaC) / 2
    else:
        novaMedia = (notaA + notaC) / 2

    if novaMedia >= 6.0:
        return "APROVADO", novaMedia
    else:
        return "REPROVADO", novaMedia

#FUNÇÃO PRINCIPAL
def main():
    numAlunos = int(input("Digite o número de alunos: "))
    somaMedias = 0

    for i in range(1, numAlunos + 1):
        print(f"Aluno {i}:")
        notaA = float(input("Digite a nota do grau A: "))
        notaB = float(input("Digite a nota do grau B: "))

        media = notaA + (notaB * 2)/3
        somaMedias += media
        #VENDO A MÉDIA DO ALUNO
        if media >= 6.0:
            print("APROVADO")
        else:
            notaC = float(input("Digite a nota do grau C: "))
            substituir = input("Qual nota deseja substituir (A ou B)? ")
            resultado, novaMedia = calcularMedia(notaA, notaB, notaC, substituir)
            print(resultado)
            print("Nova média:", novaMedia)

    mediaGeral = somaMedias / numAlunos
    print("Média geral dos alunos:", mediaGeral)


#EXECUTANDO FUNÇÃO PRINCIPAL
main()