class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        result = []
        if s == '' : return True
        if len(s) > len(t) : return False

        j = 0
        for char in t:
            if char == s[j]:
                if j == len(s) - 1:
                    return True
                j+=1
                
        return False