def tabuada():
    while True:
        numero = int(input("Entre com um número de 1 a 9: "))
        
        if numero < 1 or numero > 9:
            print("Número inválido. Por favor, entre com um número de 1 a 9.")
            continue
        print(f"Tabuada de multiplicação do número {numero}:")
        #CONSTROI A TABUADA DO NÚMERO ESPECIFICADO
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
        opcao = input("Gostaria de calcular outro número (s/n)? ").lower()
        #PARA O PROGRAMA SE A RESPOSTA FOR NÃO
        if opcao != 's':
            break
#EXECUTANDO A FUNÇÃO
tabuada()