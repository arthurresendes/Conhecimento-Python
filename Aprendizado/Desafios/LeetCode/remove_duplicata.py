class Solution:
    def deleteDuplicates(self, head: list[int]) -> list[int]:
        lista_res = []
        for i in head:
            if i not in lista_res:
                lista_res.append(i)
        for i in range(len(head) - len(lista_res)):
            lista_res.append("_")
        return lista_res


if __name__ == "__main__":
    sol = Solution()
    print(sol.deleteDuplicates([5,7,7,8,8,10]))
    print(sol.deleteDuplicates([5,7,7,8,8,10]))
    print(sol.deleteDuplicates([1,1,2]))
    print(sol.deleteDuplicates([1,1,2,3,3]))
