class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            for j in strs:
                if char != j[i]:
                    return shortest[:i] 
        
        return shortest




        