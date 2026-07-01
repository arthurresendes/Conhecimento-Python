def tabuada_1_10(num):
    print([i * num for i in range(1,11)])


if __name__ == "__main__":
    contador = 1
    while True:
        tabuada_1_10(contador)
        contador += 1
        if contador == 11: break