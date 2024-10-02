class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        st=sorted(set(arr))
        
        hm={}
        
        for i,num in enumerate(st):
            hm[num]=i+1
            
            
        for i in range(len(arr)):
            arr[i]=hm[arr[i]]
        
        return arr