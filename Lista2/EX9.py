#valor da compra
compra = float(input('Digite qual o valor da sua compra: '))

#desconto
desconto = float(input('Digite a porcentagem de desconto: '))

#valor descontado
valorDesconto = compra * desconto / 100

#valor total
total = compra - valorDesconto

#total da compra com desconto
print('O valor que deve ser pago é de R$',total)