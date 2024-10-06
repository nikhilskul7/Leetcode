class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.weights=[]
        self.total=0
        
        for i in w:
            self.total+=i
            self.weights.append(self.total)

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.randint(1, self.total)
        low, high = 0, len(self.weights) - 1
        while low < high:
            mid = (low + high) // 2
            if target > self.weights[mid]:
                low = mid + 1
            else:
                high = mid
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()