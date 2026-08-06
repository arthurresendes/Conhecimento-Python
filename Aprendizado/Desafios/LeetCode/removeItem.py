def removendo(lista: list[int]):
    for i in range(len(lista) - 1, -1, -1):
         if lista[i] == 2:
             del lista[i]
    return lista

print(removendo([1,2,2,3,4,2]))