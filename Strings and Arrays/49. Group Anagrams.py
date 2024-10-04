class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        retval=defaultdict(list)
        
        
        for num in strs:
            
            if str(sorted(num)) in retval:
                retval[str(sorted(num))].append(num)
            else:
                 retval[str(sorted(num))]=[num]
        
        return retval.values()
        