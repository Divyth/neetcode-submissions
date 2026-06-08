class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")

        for ch in paths:
            if ch == "..":
                if stack:
                    stack.pop()
            elif ch != "" and ch != ".":
                stack.append(ch)
        return "/" + "/".join(stack)