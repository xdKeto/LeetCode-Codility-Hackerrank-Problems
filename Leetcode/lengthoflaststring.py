class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.strip()
        array = new.split(' ')

        last = array[-1]

        count  = 0
        for char in last:
            count += 1
        
        return count
        