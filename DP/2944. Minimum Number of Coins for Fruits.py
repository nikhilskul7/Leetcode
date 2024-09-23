class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        
        # Dictionary for memoization
        dp = {}
        
        def check(i, j):
            # Check if result is already computed
            if (i, j) in dp:
                return dp[(i, j)]
            # Base case: If we have processed all prices
            if i >= len(prices):
                return 0
            
            # Calculate cost if we take the current price
            take = prices[i] + check(i + 1, 2 * i + 1)
            
            # Calculate cost if we do not take the current price
            nottake = check(i + 1, j) if j >= i and i > 0 else float('inf')
            
            # Store the minimum of both choices in the dp dictionary
            dp[(i, j)] = min(take, nottake)
            return dp[(i, j)]
        
        # Start the recursive function from the first price
        return check(0, 0)
