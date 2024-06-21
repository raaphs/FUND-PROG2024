#INVENTARIO CONTENDO TODOS OS INGREDIENTES
inventario = {
    "po de fenix": 100, #g
    "essencia celestial": 50, #mL
    "raiz de dragao": 45, #g
    "orvalho lunar": 30, #mL
    "flores secas": 200, #g
    "elixir amargo": 20, #mL
    "lagrimas de unicornio": 14 #mL
}

#FUNÇÃO DE PREPARAR A POÇÃO
def prepararPocao(tipo):
    if tipo == "1": #POÇÃO DE CURA
        if inventario["po de fenix"] < 30 or inventario["essencia celestial"] < 20 or inventario["flores secas"] < 20 or inventario["lagrimas de unicornio"] < 10:
            print("Poção indisponível!!")
            
    elif tipo == "2": #POÇÃO FORÇA DA FLORESTA
        if inventario["orvalho lunar"] < 20 or inventario["raiz de dragao"] < 30 or inventario["flores secas"] < 30:
            print("Poção indisponível!!")
            return
        
    elif tipo == "3": #POÇÃO SABEDORIA DA RIQUEZA
        if inventario["essencia celestial"] < 30 or inventario["po de fenix"] < 50:
            print("Poção indisponível!!")
            return
        
    elif tipo == "4": #POÇÃO SORTE NO AMOR
        if inventario["orvalho lunar"] < 10 or inventario["flores secas"] < 50 or inventario["lagrimas de unicornio"] < 5:
            print("Poção indisponível!!")
            return
        
    elif tipo == "5": #POÇÃO MALVADA
        if inventario["elixir amargo"] < 10 or inventario["raiz de dragao"] < 15:
            print("Poção indisponível!!")
            return
        
    print("Sua poção está pronta!!")

    #REDUZINDO OS INGREDIENTES DO INVENTÁRIO
    if tipo == "1":
        inventario["po de fenix"] -= 30
        inventario["essencia celestial"] -= 20
        inventario["flores secas"] -= 20
        inventario["lagrimas de unicornio"] -= 10
    elif tipo == "2":
        inventario["orvalho lunar"] -= 20
        inventario["raiz de dragao"] -= 30
        inventario["flores secas"] -= 30
    elif tipo == "3":
        inventario["essencia celestial"] -= 30
        inventario["po de fenix"] -= 50
    elif tipo == "4":
        inventario["orvalho lunar"] -= 10
        inventario["flores secas"] -= 50
        inventario["lagrimas de unicornio"] -= 5
    elif tipo == "5":
        inventario["elixir amargo"] -= 10
        inventario["raiz de dragao"] -= 15
        
#FUNÇÃO QUE CONSULTA A QUANTIDADE DE INGREDIENTES
def consultarQnt(ingrediente):
    quantidade = inventario.get(ingrediente)
    if quantidade is not None:
        print(f"Quantidade de {ingrediente}: {quantidade}g/ml.")
    else:
        print("Ingrediente não encontrado.")

#FUNÇÃO QUE SAI DO MENU
def sair():
    print("Você saiu!")
    
#FUNÇÃO QUE EXIBE O MENU
def exibirMenu():
    print("\nMenu Principal:")
    print("a) Preparar Poção")
    print("b) Consultar os Ingredientes")
    print("c) Sair")
    
#FUNÇÃO PRINCIPAL
def main():
    while True:
        exibirMenu()
        opcao = input("Escolha uma opção: ")
        if opcao == 'a':
            tipo = input("Digite qual poção você deseja(1 - POÇÃO DE CURA, 2 - POÇÃO FORÇA DA FLORESTA, 3 - POÇÃO SABEDORIA DA RIQUEZA, 4 - POÇÃO SORTE NO AMOR, 5 - POÇÃO MALVADA): ").lower()
            prepararPocao(tipo)
        elif opcao == 'b':
            ingrediente = input("Digite o ingrediente a ser consultado: ").lower()
            consultarQnt(ingrediente)
        elif opcao == 'c':
            sair()
            break
        else:
            print("Opção inválida. Tente outra opção!!")
main()