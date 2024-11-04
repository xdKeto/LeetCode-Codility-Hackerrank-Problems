class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in "({[":
                stack.append(char)
            else: 
                if not stack:
                    return False
                else:
                    popp = stack.pop()
                    if popp != brackets[char]:
                        return False
        
        return not stack

       
        
        