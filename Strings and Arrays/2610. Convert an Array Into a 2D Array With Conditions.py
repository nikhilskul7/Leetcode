    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ct=Counter(nums)
        retval=[]
        while ct:
            
            temp=[]
            for key in list(ct.keys()):
                temp.append(key)
                ct[key]-=1
                if ct[key]==0:
                    del ct[key]

            retval.append(temp)
            
        return retval
                