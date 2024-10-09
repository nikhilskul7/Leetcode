
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mp={
            "1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        retval=[]
        ans=[]
        if not digits:
            return []
        def check(i,ans):
            if i ==len(digits):
                retval.append("".join(ans[:]))
                return
            
            for j in range(len(mp[digits[i]])):
                ans.append(mp[digits[i]][j])
                check(i+1,ans)
                ans.pop()
        
        
        
        
        check(0,ans)
        return retval