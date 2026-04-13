class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = int(num1) * int(num2)
        return f' "{str(res)}" '


if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply("2","3"))
    print(sol.multiply("123","456"))