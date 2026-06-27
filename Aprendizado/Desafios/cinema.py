cadeiras = {1: 'Livre', 2: 'Ocupado', 3: 'Livre'}

def lista_lugares():
    for i,j in cadeiras.items():
        print(f"Cadeira: {i} - {j}")

def comprar_lugar(assento: int):
    if cadeiras[assento] and cadeiras[assento] == 'Livre':
        cadeiras[assento] = 'Ocupado'
        return f'Cadeira reservada, {cadeiras}'
    else:
        return 'Assento já ocupado'

if __name__ == "__main__":
    while True:
        lista_lugares()
        try:
            assento = int(input("Digite o assento desejado: "))
            if assento > 0 or assento <=len(cadeiras):
                res = comprar_lugar(assento)
                print(res)
                if res != 'Assento já ocupado':
                    break
        except:
            print("Digite um número válido")