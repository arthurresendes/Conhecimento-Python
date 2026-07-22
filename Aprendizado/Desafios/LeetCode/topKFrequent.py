class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        valores = {}
        lista = []
        for i in nums:
            if i in valores:
                valores[i] += 1
            else:
                valores[i] = 1
        for _ in range(k):
            if not valores:
                break
            maior_atual = max(valores, key=valores.get)
            lista.append(maior_atual)
            del valores[maior_atual]
        return lista


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,2,3,4],2))
    print(sol.topKFrequent([1,5,2,2,3,4],1))
    print(sol.topKFrequent([1,1,2,3,4,2,3,4,2,3,24,3,3,4,3,4,3,2,1,4,2,4,3,2,4,3,2,5,6,5,7,7,8,9,7,6,8,0,7,5,4,5,6,3,2],5))