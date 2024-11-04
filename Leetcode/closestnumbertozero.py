class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        result = nums[0]

        for i in nums:
            if abs(i) < abs(result):
                result = i
            elif abs(i) == abs(result):
                result = max(i, result)
        
        return result



        