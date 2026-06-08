class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def getCombination(i, currentArray, remaining):
            if remaining == 0 :
                res.append(currentArray.copy())
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue

                if candidates[j] > remaining :
                    break

                currentArray.append(candidates[j])
                getCombination(j+1, currentArray, remaining - candidates[j])
                
                currentArray.pop()

        getCombination(0,[],target)
        return res


            
        