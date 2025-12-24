class Solution(object):
    def maxProfit(self, prices):
        maxprices=0
        minprices=prices[0]
        for i in prices:
            if i < minprices:
                minprices=i
            else:
                maxprices=max(maxprices,i-minprices)
        return maxprices