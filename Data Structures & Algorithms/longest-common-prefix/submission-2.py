class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # the below can be considered brute force beacuse for sorting and this compare the 
        # first and last word since we thier characters match all the other words character will also match
        
        # if len(strs) == 1:
        #     return strs[0]

        # strs = sorted(strs)
        # for i in range(min(len(strs[0]), len(strs[-1]))):
        #     if strs[0][i] != strs[-1][i]:
        #         return strs[0][:i]

        # return strs[0]


        # vertical scanning most commaon 
        # flight
        # flow
        # flower

        base = strs[0]
        for i in range(len(base)):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[0:i]

        return strs[0]