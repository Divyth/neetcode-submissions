class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin = 0
        openMax = 0

        for ch in s:
            if ch == "(":
                openMin += 1
                openMax += 1

            elif ch == ")":
                openMin -= 1
                openMax -= 1
            
            # when '*' for openMax we take '(' and OpenMin we consider ")"
            else:
                openMin -= 1
                openMax += 1

            openMin = max(openMin, 0)
            if openMax < 0:
                return False

        return openMin == 0
                
