class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arrayP = list(pattern)
        arrayS = s.split(' ')

        if len(arrayP) != len(arrayS):
            return False

        char = {}
        word = {}

        for i, j in zip(arrayP, arrayS):

            if i in char:
                if char[i] != j:
                    return False
            else:
                char[i] = j
            
            if j in word:
                if word[j] != i:
                    return False
            else:
                word[j] = i
        
        return True
        

        
        

        