class Solution:
    def addBinary(self, a: str, b: str) -> str:
        soma = int(a, 2) + int(b, 2)
        return str(format(soma, 'b'))


sol = Solution()
print(sol.addBinary("11","1"))