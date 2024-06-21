#CALCULANDO PRECO DO PRODUTO
def calcular_preco_final(preco_etiqueta, forma_pagamento):
    if forma_pagamento == 1:
        return preco_etiqueta * 0.85 #15% DE DESCONTO
    elif forma_pagamento == 2:
        return preco_etiqueta * 0.90 #10% DE DESCONTO
    elif forma_pagamento == 3:
        return preco_etiqueta #SEM JUROS
    elif forma_pagamento == 4:
        return preco_etiqueta * 1.10 #10% DE JUROS
    else:
        print("Opção de pagamento inválida!!")
        return None
    
#RECEBENDO INFORMAÇÔES DOS PREÇOS
preco_etiqueta = float(input("Digite o preço normal de etiqueta do produto: R$ "))
forma_pagamento = float(input("Escolha a forma de pagamento (1 - À vista em dinheiro, 2 - À vista no cartão de crédito, 3 - Em duas vezes, 4 - Em três vezes): "))

#PREÇO FINAL DO PRODUTO
preco_final = calcular_preco_final(preco_etiqueta, forma_pagamento)
if preco_final is not None:
    print("O preço a ser pago pelo produto é: R$",preco_final)