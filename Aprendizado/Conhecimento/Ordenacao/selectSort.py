lista = [9,4,6,2,1,6,8,9]
newLista = []

while lista:
    menor = lista[0]

    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]

    newLista.append(menor)
    lista.remove(menor)

print(newLista)