class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        
        length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[length] = nums[i]
                length += 1
        
        return length


        