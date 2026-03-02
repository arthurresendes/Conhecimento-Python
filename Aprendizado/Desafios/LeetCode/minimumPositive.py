class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        menor = min(nums)
        if menor != 0 and menor != 1 and menor > 0:
            res = 1
            return res
        else:
            maximo = max(nums)
            if menor < 0:
                menor = 1
            for i in range(menor,maximo+2):
                if i in nums:
                    pass
                else:
                    return i

if __name__ == "__main__":
    sol = Solution()
    print(sol.firstMissingPositive([2,3,4]))
    print(sol.firstMissingPositive([0,1,2,3,4,7,8,9,11]))
    print(sol.firstMissingPositive([0,2,7,8,9,11]))
    print(sol.firstMissingPositive([1,2,0,3]))
    print(sol.firstMissingPositive([3,4,1,-1,2]))
