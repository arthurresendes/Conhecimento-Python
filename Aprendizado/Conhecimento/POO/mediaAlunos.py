class Aluno:
    def __init__(self,matricula: str,nome: str,nota1: float,nota2: float,nota3: float):
        self.__matricula = matricula
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2
        self.__nota3 = nota3
   
    def ver_media(self):
        media = (self.__nota1 + self.__nota2 + self.__nota3)/3
        if media >= 6.0:
            return f'Passou com a media: {media}'
        else:
            lista_provas = [self.__nota1,self.__nota2,self.__nota3]
            lista_provas.remove(min(lista_provas))
            soma_maiores = sum(lista_provas)
            nota_achar = 18.0 - soma_maiores
            return f'Você vai ter que tirar {nota_achar:.2f} na Prova substituitiva'
   
if __name__ == '__main__':
    alun1 = Aluno('1234', 'Arthur',7.0,5.0,5.5)
    print(alun1.ver_media())