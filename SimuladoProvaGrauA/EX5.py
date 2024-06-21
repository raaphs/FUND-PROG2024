estoque = {
    "cafe": 1000,  # 1000g de café
    "agua": 1000,  # 1000ml de água
    "leite": 1000,  # 1000ml de leite
    "cappuccino": 1000  # 1000g de mistura para cappuccino
}
preco = {
    "preto": 1.00,
    "com leite": 1.50,
    "cappuccino": 2.00
}

def trocar_refil(ingrediente):
    estoque[ingrediente] = 1000
    print(f"Refil de {ingrediente} trocado. Compartimento agora com 1000g/1000ml.")

def consultar_quantidade(ingrediente):
    quantidade = estoque.get(ingrediente)
    if quantidade is not None:
        print(f"Quantidade de {ingrediente}: {quantidade}g/1000ml.")
    else:
        print("Ingrediente não encontrado.")

def preparar_cafe(tipo, dinheiro):
    if tipo not in preco:
        print("Opção de café inválida.")
        return

    preco_cafe = preco[tipo]
    if dinheiro < preco_cafe:
        print("Dinheiro insuficiente.")
        return

    if tipo == "preto":
        if estoque["cafe"] < 15 or estoque["agua"] < 250:
            print("Produto indisponível. Dinheiro devolvido.")
            
    elif tipo == "com leite":
        if estoque["cafe"] < 20 or estoque["leite"] < 250:
            print("Produto indisponível. Dinheiro devolvido.")
            return
    elif tipo == "cappuccino":
        if estoque["cappuccino"] < 40 or estoque["agua"] < 300:
            print("Produto indisponível. Dinheiro devolvido.")
            return

    troco = dinheiro - preco_cafe
    print("Café pronto. Retire sua bebida!")
    print(f"Troco: R${troco:.2f}")

    # Reduzir ingredientes do estoque
    if tipo == "preto":
        estoque["cafe"] -= 15
        estoque["agua"] -= 250
    elif tipo == "com leite":
        estoque["cafe"] -= 20
        estoque["leite"] -= 250
    elif tipo == "cappuccino":
        estoque["cappuccino"] -= 40
        estoque["agua"] -= 300

def desligar():
    print("Máquina desligada.")

# Função para exibir o menu
def exibir_menu():
    print("\nMENU PRINCIPAL")
    print("a) Trocar refil")
    print("b) Consultar quantidade de ingrediente")
    print("c) Preparar café")
    print("d) Desligar")

# Função principal
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").lower()

        if opcao == "a":
            ingrediente = input("Digite o ingrediente a ser trocado: ").lower()
            trocar_refil(ingrediente)
        elif opcao == "b":
            ingrediente = input("Digite o ingrediente a ser consultado: ").lower()
            consultar_quantidade(ingrediente)
        elif opcao == "c":
            tipo = input("Digite o tipo de café (preto, com leite, cappuccino): ").lower()
            dinheiro = float(input("Digite o valor em dinheiro: "))
            preparar_cafe(tipo, dinheiro)
        elif opcao == "d":
            desligar()
            break
        else:
            print("Opção inválida. Tente novamente.")

#if _name_ == "_main_":z
main()