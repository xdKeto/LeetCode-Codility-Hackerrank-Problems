class Solution:
    def romanToInt(self, s: str) -> int:
        solution = 0
        map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        stringMap = []

        for char in s:
           if char in map:
                stringMap.append(map[char])
                
        
        for i in range(len(stringMap)):
            if i < len(stringMap) - 1 and stringMap[i] < stringMap[i+1]:
                solution -= stringMap[i]
            else:
                solution += stringMap[i]
        
        return solution


        


        