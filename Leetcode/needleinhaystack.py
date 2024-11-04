class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        h = len(haystack)

        if l > h : return -1
        if l == 0 : return 0

        for i in range(h - l + 1):
            if haystack[i:i + l] == needle:
                return i
        
        return -1
            
                
        