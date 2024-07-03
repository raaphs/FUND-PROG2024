import os
import csv
from pathlib import Path

#CAMINHO DO ARQUIVO CSV
documentos_path = Path.home() / "Documents"
nome_arquivo = 'gatinhos.csv'

#CABEÇALHO
cabecalho = ['Nome', 'Sexo', 'Idade', 'Raça', 'Cor Predominante', 'Castrado', 'FIV+', 'FELV+', 'Data de Resgate',
             'Adotado', 'Lar Temporário', 'Data de Adoção/Hospedagem', 'Tutor', 'Contato', 'Data da Última Vacina',
             'Data da Última Desvermifugação', 'Data do Último Antipulgas', 'Informações Extras']

#VERIFICA SE O ARQUIVO EXISTE, SE NÃO ELE É CRIADO
if not os.path.exists(nome_arquivo):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=cabecalho)
        writer.writeheader()

#FUNÇÃO QUE CARREGA OS DADOS DO ARQUIVO CSV
def carregar_dados(nome_arquivo):
    felinos = []
    with open(nome_arquivo, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            felinos.append(row)
    return felinos

#CARREGANDO OS DADOS AO INICIAR
felinos = carregar_dados(nome_arquivo)

#EXIBIÇÃO DO MENU
def exibir_menu():
    print("Menu Principal")
    print("1) Cadastrar felino")
    print("2) Alterar status de felino")
    print("3) Consultar informações sobre felino")
    print("4) Apresentar estatísticas gerais")
    print("5) Filtragem de dados")
    print("6) Salvar")
    print("7) Sair do programa")

#GERENCIAMENTO DO MENU
def menu_principal():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_felino()
        elif opcao == '2':
            alterar_status_felino()
        elif opcao == '3':
            consultar_felino()
        elif opcao == '4':
            apresentar_estatisticas()
        elif opcao == '5':
            filtragem_dados()
        elif opcao == '6':
            salvar_dados(nome_arquivo)
        elif opcao == '7':
            salvar_dados(nome_arquivo)
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

#CADASTRO DE UM NOVO FELINO
def cadastrar_felino():
    felino = {}
    felino['Nome'] = input("Nome: ")
    felino['Sexo'] = input("Sexo (M/F): ")
    felino['Idade'] = input("Idade: ")
    felino['Raça'] = input("Raça: ")
    felino['Cor Predominante'] = input("Cor Predominante: ")
    felino['Castrado'] = input("Castrado (Sim/Não): ")
    felino['FIV+'] = input("FIV+ (Sim/Não): ")
    felino['FELV+'] = input("FELV+ (Sim/Não): ")
    felino['Data de Resgate'] = input("Data de Resgate (dd/mm/aaaa): ")
    felino['Adotado'] = input("Adotado (Sim/Não): ")
    felino['Lar Temporário'] = input("Lar Temporário (Sim/Não): ")
    felino['Data de Adoção/Hospedagem'] = input("Data de Adoção/Hospedagem (dd/mm/aaaa): ")
    felino['Tutor'] = input("Tutor: ")
    felino['Contato'] = input("Contato: ")
    felino['Data da Última Vacina'] = input("Data da Última Vacina (dd/mm/aaaa): ")
    felino['Data da Última Desvermifugação'] = input("Data da Última Desvermifugação (dd/mm/aaaa): ")
    felino['Data do Último Antipulgas'] = input("Data do Último Antipulgas (dd/mm/aaaa): ")
    felino['Informações Extras'] = input("Informações Extras: ")
    
    felinos.append(felino)
    print("Felino cadastrado com sucesso!")

#LISTA DOS FELINOS CADASTRADOS
def listar_felinos():
    for i, felino in enumerate(felinos, start=1):
        print(f"{i}) {felino['Nome']}")

#ALTERA O STATUS DE ALGUM FELINO
def alterar_status_felino():
    listar_felinos()
    index = int(input("Escolha o número do felino que deseja alterar: ")) - 1
    felino = felinos[index]
    
    print("Escolha a informação que deseja alterar:")
    for i, (chave, valor) in enumerate(felino.items(), start=1):
        print(f"{i}) {chave}: {valor}")
    
    while True:
        opcao = input("Número da informação a alterar (ou '0' para voltar ao menu): ")
        if opcao == '0':
            break
        else:
            chave = list(felino.keys())[int(opcao) - 1]
            novo_valor = input(f"Novo valor para {chave}: ")
            felino[chave] = novo_valor
            print(f"{chave} atualizado para {novo_valor}")

#CINSULTA DE INFORMAÇÕES DE FELINOS
def consultar_felino():
    listar_felinos()
    index = int(input("Escolha o número do felino que deseja consultar: ")) - 1
    felino = felinos[index]
    
    for chave, valor in felino.items():
        print(f"{chave}: {valor}")

#APRESENTAÇÃO DAS ESTATÍSTICAS GERAIS 
def apresentar_estatisticas():
    total = len(felinos)
    machos = sum(1 for felino in felinos if felino['Sexo'] == 'M')
    femeas = total - machos
    adotados = sum(1 for felino in felinos if felino['Adotado'].lower() == 'sim')
    nao_adotados = total - adotados
    
    fiv_neg = sum(1 for felino in felinos if felino['FIV+'].lower() == 'não')
    felv_neg = sum(1 for felino in felinos if felino['FELV+'].lower() == 'não')
    apenas_fiv = sum(1 for felino in felinos if felino['FIV+'].lower() == 'sim' and felino['FELV+'].lower() == 'não')
    apenas_felv = sum(1 for felino in felinos if felino['FIV+'].lower() == 'não' and felino['FELV+'].lower() == 'sim')
    ambos = sum(1 for felino in felinos if felino['FIV+'].lower() == 'sim' and felino['FELV+'].lower() == 'sim')
    
    print("Estatísticas Gerais:")
    print(f"Porcentagem de machos: {machos / total * 100:.2f}%")
    print(f"Porcentagem de fêmeas: {femeas / total * 100:.2f}%")
    print(f"Porcentagem de adotados: {adotados / total * 100:.2f}%")
    print(f"Porcentagem de não adotados: {nao_adotados / total * 100:.2f}%")
    print(f"Porcentagem de felinos FIV-: {fiv_neg / total * 100:.2f}%")
    print(f"Porcentagem de felinos FELV-: {felv_neg / total * 100:.2f}%")
    print(f"Porcentagem de felinos apenas FIV+: {apenas_fiv / total * 100:.2f}%")
    print(f"Porcentagem de felinos apenas FELV+: {apenas_felv / total * 100:.2f}%")
    print(f"Porcentagem de felinos FIV+ e FELV+: {ambos / total * 100:.2f}%")

#FILTRAR OS GATOS POR PERÍODO
def filtrar_gatos_por_periodo(tipo):
    ano_inicio = int(input("Ano de início: "))
    ano_fim = int(input("Ano de fim: "))
    
    if tipo == 'resgate':
        campo = 'Data de Resgate'
    elif tipo == 'adocao':
        campo = 'Data de Adoção/Hospedagem'
    
    for felino in felinos:
        data = felino[campo]
        if data != '':
            ano = int(data.split('/')[-1])
            if ano_inicio <= ano <= ano_fim:
                for chave, valor in felino.items():
                    print(f"{chave}: {valor}")
                print()

#FUNÇÃO QUE GERENCIA O FILTRO DE GATOS
def filtragem_dados():
    print("Filtragem de Dados:")
    print("1) Consultar gatos resgatados por período")
    print("2) Consultar gatos adotados por período")
    
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        filtrar_gatos_por_periodo('resgate')
    elif opcao == '2':
        filtrar_gatos_por_periodo('adocao')
    else:
        print("Opção inválida. Tente novamente.")

#SALVAMENTO DOS DADOS NO ARQUIVO CSV
def salvar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=cabecalho)
            writer.writeheader()
            writer.writerows(felinos)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

if __name__ == '__main__':
    menu_principal()