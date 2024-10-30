tamanhoCidade = 0
#tamanhoTerritorial = 0
#tamanhoPopulacao = 0

nomeCidade = []
dimTerritorial = []
qtdPopulacao = []


#interface
def criaDados():
    nCid = str(input("|    nome da cidade: "))
    dTer = int(input("|    dimensão territorial (em kms): "))
    pop = int(input("|    população: "))
    inserirDados(nCid,dTer,pop)


def inserirDados(nCid, dTer, pop):
    if nCid == "":
        print("|    nao foi inserido um nome para cidade")
        menu()
    if dTer == "" or dTer <= 0:
        print("|    nao foi inserido uma dimensao do territorio")
        menu()
    if pop == "" or pop <= 0:
        print("|    quantidade da populacao invalida")
        menu()
    if len(nomeCidade) < 100:
        nomeCidade.append(nCid)
        dimTerritorial.append(dTer)
        qtdPopulacao.append(pop)    

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
    print(f'|    a cidade mais extensa tem o nome de {cidade} com a dimensao de {maior} kms')


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
    print(f'|    a cidade mais populosa tem o nome de {cidade} com a populacao de {maior} habitantes')

def mediaPopulacao():
    if not qtdPopulacao:
        print("|    Nenhuma cidade cadastrada")
        return
    
    media = sum(qtdPopulacao)/len(nomeCidade)  
    print('|    A media das cidades é de ', media)

def lerDados():
    cidade = ""
    populacao = 0
    tamanhoTer = 0
    
    cidade = str(input("|    DIGITE O NOME DA CIDADE: "))
    for i in range(len(nomeCidade)):
        if(cidade == nomeCidade[i]):
            populacao = qtdPopulacao[i]
            tamanhoTer = dimTerritorial[i]
            print(f'|    nome: {cidade}  \n|    populacao: {populacao} \n|    dimensão territorial: {tamanhoTer}')
            return
    print("|    Cidade não encontrada")

def menu():
    #while True:
        print()
        print("╭––––––––––––––––––––––––––––––––––––––––––––––––––––––––––╮")
        print("|    APS             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⎯⠀⠀❐⠀⠀⤬")
        print("┞––––––––––––––––––––––––––––––––––––––––––––––––––––––––––┦")
        print("|    selecione a funcao desejada:")
        print("|    1 - Inserir dados")
        print("|    2 - Cidade Mais Populosa")
        print("|    3 - Cidade Mais extensa")
        print("|    4 - Media População")
        print("|    5 - Ler Dados")   
        print("|    6 - fechar programa")   
        print("|")
        print("|")
       
        res = int(input("|    Digite o numero respectivo: "))
        if(res < 1 or res > 6):
            print("|    valor invalido")
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
                print("|    programa fechado")
                print("╰––––––––––––––––––––––––––––––––––––––––––––––––––––––––––╯")
                #break

menu()
