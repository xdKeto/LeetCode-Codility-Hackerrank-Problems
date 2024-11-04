class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        i = 0

        while i < len(nums):
            start = nums[i]

            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1

            if start != nums[i]:
                string = str(start) + "->" + str(nums[i])
                result.append(string)
            else:
                string = str(start)
                result.append(string)

            i += 1

        
        return result