class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
            elif target > nums[i]:
                pass
        return len(nums)


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1,3,5,6], 5))
    print(sol.searchInsert([1,3,5,6], 7))
    print(sol.searchInsert([1,3,5,6], 2))