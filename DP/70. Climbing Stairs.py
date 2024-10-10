class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1] *( n+1)
        def recur(i):
           
            if i<0:
                return 0
            
            if i==0:
                return 1
            if dp[i]!=-1:
                return dp[i]
            dp[i]=recur(i-1)+recur(i-2)
            return dp[i]
        return recur(n)