#valores dos dispositivos
preco_phone = 1000.00
preco_tablet = 1500.00

#saber quantos dispositivos venderam durante o dia
quantidade_phone = float(input('Digite quantos smartphones foram vendidos: '))
quantidade_tablet = float(input('Digite quantos tablets foram vendidos: '))

#calcular quantidade com valor
total = (preco_phone * quantidade_phone) + (preco_tablet * quantidade_tablet)

#mostrar ao chefe o quanto foi arrecadado
print('Foram arrecadados R$',total,'durante o dia')