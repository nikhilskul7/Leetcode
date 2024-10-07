class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.hm={ i:n for i, n in enumerate(nums) if n}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        
        retval=0
        for i in vec.hm.keys():
            if  i in self.hm:
                retval+=(vec.hm[i]*self.hm[i])
        return retval

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)