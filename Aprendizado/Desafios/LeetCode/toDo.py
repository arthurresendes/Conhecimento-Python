estoqueProd = {"produtos": []}

def apresentacao():
    print("="*50)
    print("--- Bem vindo ao controle de estoque ---")
    print("="*50)

def menu():
    apresentacao()
    while True:
        print("Escolha uma das operações: ")
        print("[1] - Adicionar produto")
        print("[2] - Ver produtos")
        print("[3] - Atualizar estoque")
        print("[4] - Deletar produto")
        print("[5] - Sair")
        
        opcao = 0
        try:
            opcao = int(input("Digite uma das opções pelo indice: "))
        except:
            print("Digite um valor inteiro....")
        
        if opcao == 1:
            addProd()
        elif opcao == 2:
            seeProd()
        elif opcao == 3:
            upProd()
        elif opcao == 4:
            delProd()
        elif opcao == 5:
            print("Saindo...")
            break
        else:
            print("Opção invalida....")

def informacoesProd():
    nome = input("Digite o nome do produto: ").title()
    while True:
        try:
            preco = int(input("Digite o preço do produto: "))
            if isinstance(preco,int):
                break
        except:
            print("Digite um preço valido..")

    while True:
        try:
            quantidade = int(input("Digite a quantidade do produto: "))
            if isinstance(quantidade,int):
                break
        except:
            print("Digite uma quantidade valido..")
    
    return nome,preco,quantidade

def addProd():
    nome,preco,quantidade = informacoesProd()
    
    lista = [nome,preco,quantidade]
    estoqueProd["produtos"].append(lista)
    print("Produto adicionado com sucesso...")

def seeProd():
    for i, item in enumerate(estoqueProd['produtos'], start=1):
        print(f"{i} - Nome: {item[0]}, Preço: {item[1]}, Quantidade: {item[2]}")

def upProd():
    seeProd()
    while True:
        try:
            indice = int(input("Digite o indice que quer atualizar o produto: ")) - 1
            if isinstance(indice,int) and indice < len(estoqueProd["produtos"]) and indice > 0:
                    nome,preco,quantidade = informacoesProd()
                    estoqueProd["produtos"][indice] = [nome, preco, quantidade]
                    break
        except:
            print("Digite um indice valido..")

def delProd():
    seeProd()
    while True:
        try:
            indice = int(input("Digite o indice que quer deletar o produto: ")) - 1
            if isinstance(indice,int) and indice < len(estoqueProd["produtos"]) and indice > 0:
                    del estoqueProd["produtos"][indice]
                    break
        except:
            print("Digite um indice valido..")


if __name__ == "__main__":
    menu()