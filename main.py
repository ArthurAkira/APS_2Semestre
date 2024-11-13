tamanhoCidade = 0
#tamanhoTerritorial = 0
#tamanhoPopulacao = 0

nomeCidade = []
dimTerritorial = []
qtdPopulacao = []


#interface
def menu():
    while True:
        print()
        print("╭––––––––––––––––––––––––––––––––––––––––––––––––––––––––––╮")
        print("|    Atividades Práticas Supervisionadas      ⠀⠀⠀⠀⠀⠀⎯⠀⠀❐⠀⠀⤬  ")
        print("┞––––––––––––––––––––––––––––––––––––––––––––––––––––––––––┦")
        print("|    Selecione a função desejada:")
        print("|    1 - Inserir Dados")
        print("|    2 - Cidade Mais Populosa")
        print("|    3 - Cidade Mais extensa")
        print("|    4 - Média População")
        print("|    5 - Ler Dados")   
        print("|    6 - fechar programa")   
        print("|")
        print("|")
       
        res = int(input("|    Digite o número respectivo: "))
        if(res < 1 or res > 6):
            print("|    Valor Inválido")
            menu()

        print("|")
        print("|")
    
        match res:
            case 1:
                criaDados()
            case 2:
                cidadeMaisPopulosa()
            case 3:
                cidadeMaisExtensa()
            case 4:
                mediaPopulacao()
            case 5:
                lerDados()
            case 6:
                print("|    Programa Fechado")
                print("╰––––––––––––––––––––––––––––––––––––––––––––––––––––––––––╯")
                quit()

def criaDados():
    nCid = str(input("|    Nome da cidade: "))

    for i in range(len(nomeCidade)):
        if(nCid == nomeCidade[i]):
            print("|    Cidade já existente")
            return

    dTer = int(input("|    Dimensão territorial (em km²): "))
    pop = int(input("|    População: "))
    inserirDados(nCid,dTer,pop)


def inserirDados(nCid, dTer, pop):
    if nCid == "":
        print("|    Não foi inserido um nome para cidade")
        return
    if dTer == "" or dTer <= 0:
        print("|    Não foi inserido uma dimensão do território")
        return
    if pop == "" or pop <= 0:
        print("|    Quantidade da população inválida")
        return
    
    if len(nomeCidade) < 100:
        nomeCidade.append(nCid)
        dimTerritorial.append(dTer)
        qtdPopulacao.append(pop)
        print("|    DADOS INSERIDOS")
        con = input("|    Pressione enter para continuar")    

def cidadeMaisExtensa():
    if not nomeCidade:
        print("|    Nenhuma cidade cadastrada")
        return

    maior = dimTerritorial[0]
    cidade = nomeCidade[0]
    for i in range(len(dimTerritorial)):
        if(maior < dimTerritorial[i]):
            maior = dimTerritorial[i]
            cidade = nomeCidade[i]
    print(f'|    A cidade mais extensa tem o nome de {cidade} com a dimensão de {maior} kms')
    con = input("|    Pressione enter para continuar")


def cidadeMaisPopulosa():
    if not nomeCidade:
        print("|    Nenhuma cidade cadastrada")
        return

    maior = qtdPopulacao[0]
    cidade = nomeCidade[0]
    for i in range(len(qtdPopulacao)):
        if(maior < qtdPopulacao[i]):
            maior = qtdPopulacao[i]
            cidade = nomeCidade[i]
    print(f'|    A cidade mais populosa tem o nome de {cidade} com a população de {maior} habitantes')
    con = input("|    Pressione enter para continuar")

def mediaPopulacao():
    if not qtdPopulacao:
        print("|    Nenhuma cidade cadastrada")
        return
    
    media = sum(qtdPopulacao)/len(nomeCidade)  
    print('|    A média das cidades é de ', media)
    con = input("|    Pressione enter para continuar")

def lerDados():
    cidade = ""
    populacao = 0
    tamanhoTer = 0
    print("|    Seleciona uma opção: ")
    print("|    1 - Ler todos os dados")
    print("|    2 - Ler um dado específico") 
    res = int(input("|    Resposta: "))
    print("┞––––––––––––––––––––––––––––––––––––––––––––––––––––––––––┦   ")
    match res:
        case 1:
            for i in range(len(nomeCidade)):
                cidade = nomeCidade[i]
                populacao = qtdPopulacao[i]
                tamanhoTer = dimTerritorial[i]
                print(f'|    nome: {cidade}  \n|    população: {populacao} \n|    dimensão territorial: {tamanhoTer}')
                print("┞––––––––––––––––––––––––––––––––––––––––––––––––––––––––––┦   ")
            con = input("|    Pressione enter para continuar")

            return   
        case 2:
            cidade = str(input("|    DIGITE O NOME DA CIDADE: "))
            for i in range(len(nomeCidade)):
                if(cidade == nomeCidade[i]):
                    populacao = qtdPopulacao[i]
                    tamanhoTer = dimTerritorial[i]
                    print(f'|    nome: {cidade}  \n|    população: {populacao} \n|    dimensão territorial: {tamanhoTer}')
                    con = input("|    Pressione enter para continuar")
                    return
            print("|    Cidade não encontrada")

menu()
