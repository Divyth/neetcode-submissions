class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        res = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(index, subset):
            if index == len(digits):
                res.append("".join(subset))
                return

            for ch in digitToChar[digits[index]]:
                subset.append(ch)
                backtrack(index + 1, subset)
                subset.pop()

        backtrack(0, [])
        return res