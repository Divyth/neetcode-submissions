class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        if not temperatures:
            return res
        for i in range(len(temperatures)):
            found = False
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    res.append(j-i)
                    found = True
                    break
            if not found:
                res.append(0)
                
            
                    
            
        return res
                    