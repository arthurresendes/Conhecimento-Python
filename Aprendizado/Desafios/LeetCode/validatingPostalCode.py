def validation(number: int):
    if number < 10000 or number > 999999:
        return "Erro, o numero tem que ser entre 100000 até 999999"
    
    number = str(number)
    list_number = [i for i in number]
    list_result = []
    
    for i in range(len(list_number)):
        if i == 4:
            break
        elif list_number[i] == list_number[i+2]:
            if list_number[i] in list_result:
                pass
            else:
                list_result.append(list_number[i])
                list_result.sort()

    if len(list_result) > 0:
        return f"Existe digitos alternativos, o(s) numero(s) são: {[int(i) for i in list_result]}"
    else:
        return "Sem digitos alternativos"

if __name__ == "__main__":
    print(validation(121426))
    print(validation(523563))
    print(validation(552523))
    print(validation(121202))