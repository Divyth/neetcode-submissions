class Solution:
    def decodeString(self, s: str) -> str:
        count = []
        string = []

        resString = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                string.append(resString)
                count.append(k)
                resString = ""
                k = 0
            elif c =="]":
                tmp = resString
                resString = string.pop()
                cur_digit = count.pop()
                resString += tmp * cur_digit
            else:
                resString += c
        return resString
                