class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # bisa pake for juga, lebih cepet runtime
        i = 0
        while True:
            if i not in nums:
                return i
            i += 1
        