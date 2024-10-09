class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        
        retval=[]
        
        def dfs(left,right,retval,ans):
            if len(ans)==n*2:
                retval.append(ans)
                return
            if left<n:
                dfs(left+1,right,retval,ans+"(")
            if right<left:
                dfs(left,right+1,retval,ans+")")
        
        ans=""
        dfs(0,0,retval,ans)
        return retval
                
        