class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        numberStr = ""
        for i in range(len(digits)):
            numberStr = numberStr + str(digits[i])
        
        numberInt = int(numberStr) + 1
        numberStr = str(numberInt)
        newList = []
        for i in numberStr:
            newList.append(int(i))
        return newList


if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1,2,3]))
    print(sol.plusOne([4,3,2,1]))
    print(sol.plusOne([9]))