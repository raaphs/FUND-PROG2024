#valor de cada produto
camiseta = 25.00
calca = 100.00
cinto = 40.00

#perguntar ao cliente a quantidade de produtos
qntCamiseta = int(input('Digite quantas camisetas serão compradas: '))
qntCalca = int(input('Digite quantas calças serão compradas: '))
qntCinto = int(input('Digite quantos cintos serão comprados: '))

#desconto
desconto = 10.00

#calculo da compra sem desconto
qntCompra = (qntCinto * cinto) + (qntCamiseta * camiseta) + (qntCalca * calca)

#valor final com desconto
valorDesconto = qntCompra * desconto/100

#total a ser pago
total = qntCompra - valorDesconto
print('Valor do desconto foi de',desconto,'%')
print('Seu valor com o desconto especial ficou em R$',total)