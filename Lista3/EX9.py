#Definindo as variaveis
def converter_real_para_euro(valor, cotacao_real_euro):
    return valor / cotacao_real_euro

def converter_real_para_dolar(valor, cotacao_real_dolar):
    return valor / cotacao_real_dolar

def converter_euro_para_dolar(valor, cotacao_euro_dolar):
    return valor * cotacao_euro_dolar

def converter_euro_para_real(valor, cotacao_euro_real):
    return valor * cotacao_euro_real

def converter_dolar_para_euro(valor, cotacao_dolar_euro):
    return valor / cotacao_dolar_euro

def converter_dolar_para_real(valor, cotacao_dolar_real):
    return valor * cotacao_dolar_real

#Definindo os valores de cotação
cotacao_real_dolar = float(input("Digite a cotação do dólar em relação ao real: "))
cotacao_real_euro = float(input("Digite a cotação do euro em relação ao real: "))
cotacao_euro_dolar = cotacao_real_euro / cotacao_real_dolar

#CONSTRUINDO O MENU
print("\nMenu:")
print("1) Converter de Real para Euro")
print("2) Converter de Real para Dólar")
print("3) Converter de Euro para Dólar")
print("4) Converter de Euro para Real")
print("5) Converter de Dólar para Euro")
print("6) Converter de Dólar para Real")

opcao = int(input("\nEscolha a opção desejada: "))

#Construindo as opções
if opcao == 1:
    valor_real = float(input("Digite o valor em reais: R$ "))
    resultado = converter_real_para_euro(valor_real, cotacao_real_euro)
    print("Valor em euros: ",resultado)
elif opcao == 2:
    valor_real = float(input("Digite o valor em reais: R$ "))
    resultado = converter_real_para_dolar(valor_real, cotacao_real_dolar)
    print("Valor em dólares: ",resultado)
elif opcao == 3:
    valor_euro = float(input("Digite o valor em euros: € "))
    resultado = converter_euro_para_dolar(valor_euro, cotacao_euro_dolar)
    print("Valor em dólares: ",resultado)
elif opcao == 4:
    valor_euro = float(input("Digite o valor em euros: € "))
    resultado = converter_euro_para_real(valor_euro, cotacao_real_euro)
    print("Valor em reais: ",resultado)
elif opcao == 5:
    valor_dolar = float(input("Digite o valor em dólares: $ "))
    resultado = converter_dolar_para_euro(valor_dolar, cotacao_euro_dolar)
    print("Valor em euros: ",resultado)
elif opcao == 6:
    valor_dolar = float(input("Digite o valor em dólares: $ "))
    resultado = converter_dolar_para_real(valor_dolar, cotacao_real_dolar)
    print("Valor em reais: ",resultado)
else:
    print("Opção inválida!!")