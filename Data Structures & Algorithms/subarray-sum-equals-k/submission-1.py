class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        count = 0
        prefixMap = {0:1} # initailized with {0:1} ie prefixSum of 0 with count 1, 
        # if their may be a case if prefixSum - k == 0, so their will be no value 
        # in the hashmap might return invalid


        for num in nums:
            prefixSum += num

            if (prefixSum - k) in prefixMap:
                count += prefixMap[prefixSum - k]
            
            prefixMap[prefixSum] = prefixMap.get(prefixSum,0) + 1
        
        return count
            



            
        