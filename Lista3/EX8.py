#Calculando valor da venda
def calcular_valor_venda(valor_compra):
    if valor_compra < 20:
        lucro = 0.45
    elif valor_compra <=50:
        lucro = 0.35
    else:
        lucro = 0.25

    valor_venda = valor_compra * (1 + lucro)
    return valor_venda
valor_compra = float(input("Digite o valor de compra do produto: R$ "))
valor_venda = calcular_valor_venda(valor_compra)

#Valor da venda sendo informado
print("O valor de venda do produto é: R$", valor_venda)