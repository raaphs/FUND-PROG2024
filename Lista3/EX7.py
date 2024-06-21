#Cálculo do desconto
def calcular_desconto_previdenciario(salario):
    desconto_máximo = 318.20
    desconto_proporcional = salario * 0.11

    return min(desconto_proporcional, desconto_máximo)

#Definição do desconto
salario = float(input("Digite o salário do funionário: "))
desconto = calcular_desconto_previdenciario(salario)
print("O desconto previdenciario é de R$ ",desconto)
