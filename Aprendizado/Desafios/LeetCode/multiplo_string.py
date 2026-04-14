class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return f' "{str(int(num1) * int(num2))}" '


if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply("2","3"))
    print(sol.multiply("123","456"))