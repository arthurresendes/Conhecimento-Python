class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(0,n):
            num = 2 ** i
            if num == n:
                return True
            if num > n: 
                return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfTwo(16))
    print(sol.isPowerOfTwo(3))
    print(sol.isPowerOfTwo(32))
    print(sol.isPowerOfTwo(10))
    print(sol.isPowerOfTwo(1))