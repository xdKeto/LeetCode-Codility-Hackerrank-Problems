class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join(char for char in s if char.isalnum())
        result = result.lower()
        print(result)

        reverseS = list(result)
        reverseS.reverse()

        newString = ''.join(reverseS)
        print(newString)

        if(result != newString):
            return False
        else:
            return True
        