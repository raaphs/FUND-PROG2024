#DEFININDO CÉDULAS
def calcular_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 1]
    resultado = {}
    
    #CALCULO
    for cedula in cedulas:
        if valor >= cedula:
            quantidade = valor // cedula
            resultado[cedula] = quantidade
            valor -= quantidade * cedula
    
    return resultado

#DEFINIÇÂO DO VALOR DESEJADO
valor = int(input("Digite o valor desejado: R$ "))
notas = calcular_cedulas(valor)

print("Notas utilizadas:")
for cedula, quantidade in notas.items():
    print(quantidade,"nota(s) de R$",cedula)