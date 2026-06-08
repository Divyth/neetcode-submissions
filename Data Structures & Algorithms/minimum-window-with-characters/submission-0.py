class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = defaultdict(int)
        l = 0
        res = ""
        curr = 0
        goal = len(need)

        for r in range(len(s)):
            have[s[r]] += 1

            if s[r] in need and need[s[r]] == have[s[r]]:
                curr += 1
            
            while curr == goal:
                if not res or len(res) > (r - l + 1):
                    res = s[l:r+1]

                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    curr -= 1
                l += 1
        return res