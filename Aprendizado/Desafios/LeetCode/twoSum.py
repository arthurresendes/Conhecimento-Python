class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lista_duplas_result = []
        for i in range(len(nums)):
            res = 0
            res = target - nums[i]
            if res in nums:
                indice_encontrado = nums.index(res)
                if indice_encontrado != i and i < indice_encontrado:
                    lista_duplas_result.append([i, indice_encontrado])

       
        return lista_duplas_result
   

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([1,2,3,4,5,6,7,8,9], 16))
