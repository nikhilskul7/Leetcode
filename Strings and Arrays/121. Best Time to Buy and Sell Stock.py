class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        retval=0
        
        mini=prices[0]
        
        for i in range(len(prices)):

            mini=min(mini,prices[i]) 
            retval=max(retval,prices[i]-mini)
        
        return retval
    
    