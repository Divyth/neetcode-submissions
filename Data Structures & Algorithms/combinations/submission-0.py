class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(i, currentArray):
            if i > n:
                if len(currentArray) == k:
                    res.append(currentArray.copy())
                return 

           
            currentArray.append(i)
            dfs(i + 1, currentArray)
            currentArray.pop()
            dfs(i + 1, currentArray)

        dfs(1,[])

        return res


        