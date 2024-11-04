class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        array = []
        isCheap = 99999

        for i in prices:
            if i < isCheap:
                isCheap = i
            else:
                temp = i - isCheap
                array.append(temp)

        if not array:
            return 0
        else:
            result = max(array)
            return result
        