class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0 
        total = 0
        prefixMap = {0:1} # prefixSum : frequency

        for num in nums:
            prefixSum += num

            if prefixSum - k in prefixMap:
                total += prefixMap[prefixSum - k]
            
            prefixMap[prefixSum] = prefixMap.get(prefixSum, 0) + 1

        return total

            
        