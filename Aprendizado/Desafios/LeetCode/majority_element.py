class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        valores = {}
        for i in nums:
            if i not in valores:
                valores[i] = 1
            else:
                valores[i] += 1
        
        maior_valor = 0
        chave_vencedora = None
        
        for chave, valor in valores.items():
            if valor > maior_valor:
                maior_valor = valor
                chave_vencedora = chave
        
        return chave_vencedora


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([1,2,4,4,5,3]))
    print(sol.majorityElement([1,2,4,4,5,3,5,67,1,2,4,5,6,1,3,5,1,1,1]))
    print(sol.majorityElement([1,2,4,4,5,3,3,2,2,2,2,2,9]))