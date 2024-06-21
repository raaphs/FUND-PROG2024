#MEDIA
def calcular_media(nota_a, nota_b):
    return nota_a + (nota_b * 2)/3

#VERIFICANDO APROVAÇÂO
def verificar_aprovacao(media):
    if media >= 60.0:
        return "aprovado"
    else:
        return "em recuperação"

#SUBSTITUIÇÂO DA NOTA
def substituir_nota(nota_a, nota_b, grau_substituir):
    if grau_substituir == "a":
        nota_a = float(input("Digite a nota nota do Grau A: "))
    elif grau_substituir == "b":
        nota_b = float(input("Digite a nota nota do Grau B: "))
    else:
        print("Opção inválida!")
    return nota_a, nota_b

#RECEBENDO AS NOTAS
nota_a = float(input("Digite a nota do Grau A: "))
nota_b = float(input("Digite a nota do Grau B: "))

media = calcular_media(nota_a, nota_b)
print("A média final do aluno é:",media)

#SITUAÇÂO DO ALUNO
situacao = verificar_aprovacao(media)

if situacao == "aprovado":
    print("O aluno está aprovado")
else:
    print("O aluno está em recuperação")
    grau_substituir = input("DIgite 'a' para substituir a nota do Grau A ou 'b' para substituir a nota do Grau B: ").lower()
    nota_a, nota_b = substituir_nota(nota_a, nota_b, grau_substituir)
    nova_media = calcular_media(nota_a, nota_b)
    situacao = verificar_aprovacao(nova_media)

#SITUAÇÂO FINAL DO ALUNO, ULTIMA CHANCE
if situacao == "aprovado":
    print("Após a subtituição, o aluno está aprovado com média final",nova_media)
else:
    print("Após a subtituição, o aluno está reaprovado com média final",nova_media)