class Solution:
    def decodeString(self, s: str) -> str:
        stack =[]
		
        for ch in s:
            if ch != "]":
                stack.append(ch)				
            else:
                sub = ""
                while stack and stack[-1] != "[":
                    sub = stack.pop() + sub
                
                stack.pop()
				
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(int(num) * sub)

        return "".join(stack)
                