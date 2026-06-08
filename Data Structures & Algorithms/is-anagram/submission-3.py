class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = Counter(s)

        for l in t:
            if l not in counter or counter[l] == 0:
                return False
            counter[l] -=1
        return True 


                