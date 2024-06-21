#solicita o usuario o preco e o valor
preco_gasolina = float(input('Digite o preço da gasolina: R$'))
valor_disponivel = float(input('Digite o valor que deseja pagar: R$'))

#quantidade de litros que o motorista pode comprar
litros = valor_disponivel / preco_gasolina

#mostrar ao motorista o quanto conseguiu encher o tanque
print('Com R$',valor_disponivel,'você conseguiu encher o tanque com',litros,'L')