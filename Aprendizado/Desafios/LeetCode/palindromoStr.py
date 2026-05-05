class Solution:
    def isPalindromo(self,word: str):
        inicio = 0 
        fim = len(word) - 1
        while(inicio < fim):
            if word[inicio] == word[fim]:
                inicio += 1
                fim -= 1
            else:
                return "Não é palindormo"
        return "É palindromo"

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindromo("mom"))
    print(sol.isPalindromo("oi"))
    print(sol.isPalindromo("osso"))
    print(sol.isPalindromo("bola"))