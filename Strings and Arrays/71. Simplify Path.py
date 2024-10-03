class Solution:
    def simplifyPath(self, path: str) -> str:
            retval=[]
            path=path.split("/")
            for word in path:
                
                if retval and word == "..":
                    retval.pop()
                elif  word not in ["..",".",""]:
                    retval.append(word)

            
            return "/"+"/".join(retval)