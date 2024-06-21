#CRIANDO AS CATEGORIAS
def determinar_categorias(idade):
    if idade >= 5 and idade <= 7:
        return "Infantil A"
    elif idade >= 8 and idade <= 10:
        return "Infantil B"
    elif idade >= 11 and idade <= 13:
        return "Juvenil A"
    elif idade >= 14 and idade <= 17:
        return "Juvenil B"
    else:
        return "Sênior"

#PERGUNTADO A IDADE
idade = int(input("Digite a idade do nadador: "))
categoria = determinar_categorias(idade)
print("A categoria do nadadoe é:",categoria)