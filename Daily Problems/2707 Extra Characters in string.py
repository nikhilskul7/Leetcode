class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        '''
        Time Complexity: O(n*n) where n is the length of string.
        Space Complexity: O(n) where n is length of string to store the dp array.
        '''
        
        
        # Change list into set for easier lookup
        dictionary=set(dictionary)
        
        # Create array for memoization
        dp=[-1 ]* len(s)
        
        # Recursive function to check for words in substrings
        def check(i):
            
            # Terminate condition
            if i==len(s):
                return 0
            
            # Look in DP
            if dp[i]!=-1:
                return dp[i]
            
            # Don't take current character
            ans=1+check(i+1)
            
            # Search for words using substring
            for j in range(i,len(s)):
                if s[i:j+1] in dictionary:
                    ans=min(ans,check(j+1))
                    
            # Store answer in DP and return
            dp[i]=ans       
            return ans
        
        # Call the recursive function
        return check(0)
