class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freqMap = {}
        res = 0

        maxF = 0

        for r in range(len(s)):
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0) #increase the freq
            maxF = max(maxF, freqMap[s[r]]) # get the macF in the map

            while (r - l + 1) - maxF > k: # check for current window size if window deosnt have same characters greater than k 
                freqMap[s[l]] -= 1
                l += 1
            res = max(res, r - l +1)
        return res

