class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        menores = [min(i) for i in triangle]
        soma = 0
        for i in menores:
            soma +=i
        return soma

if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    print(sol.minimumTotal([[-10]]))