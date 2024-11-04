class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1, length2 = len(word1), len(word2)
        a, b = 1, 1
        print(length1, length2)

        switch = 1
        result = [word1[0], word2[0]]
        while a < length1 and b < length2:
            if switch == 1:
                result.append(word1[a])
                a += 1
                switch = 2
            else:
                result.append(word2[b])
                b += 1
                switch = 1
        
        if a < length1:
            result.append(word1[a:])
        if b < length2:
            result.append(word2[b:])

        return "".join(result)
                