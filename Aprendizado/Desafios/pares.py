def pares(start,fim):
    return f"Lista de pares: {[i for i in range(start,fim+1) if i % 2 == 0]}"

if __name__ == "__main__":
    while True:
        try:
            comeco = int(input("Digite o incio da lista: "))
            fim = int(input("Digite o fim da lista: "))
            print(pares(comeco,fim))
            break
        except: 
            print("Digite número validos")