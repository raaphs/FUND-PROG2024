#CALCULANDO O VALOR DO PLANO DE SAUDE
def calcular_valor_plano(idade_conveniado, num_dependentes):
    valor_base = 300
    valor_adicional = 0
    
    if idade_conveniado < 10:
        valor_adicional +=100
        
    for _ in range(num_dependentes):
        idade_dependente = int(input("Digite a idade do dependente: "))
        if idade_dependente < 10:
            valor_adicional += 100
        elif 10 <= idade_dependente <= 30:
            valor_adicional += 220
        elif 31 <= idade_dependente <= 60:
            valor_adicional += 395
        else:
            valor_adicional += 480
    
    return valor_base + valor_adicional

#INFORMAÇÔES INPORTANTES
idade_conveniado = int(input("Digite a idade do conveniado: "))
num_dependentes = int(input("Digite o número de dependentes: "))

#VALOR TOTAL
valor_total = calcular_valor_plano(idade_conveniado, num_dependentes)
print("O valor a ser pago pelo plano de saúde é: R$",valor_total)