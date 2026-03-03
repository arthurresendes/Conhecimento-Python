class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        inverso = nums[-target:]
        del nums[-target:]
        inverso = inverso[::-1]
        for i in range(len(inverso)):
            nums.insert(0,inverso[i])
        
        print(nums)
        return True if target in nums else False

if __name__ == "__main__":
    sol = Solution()
    print(sol.search([0,1,2,4,4,4,5,6,6,7],5))
    print(sol.search([0,1,2,4,4,4,5,6,6,7],0))
    print(sol.search([2,5,6,0,0,1,2],3))