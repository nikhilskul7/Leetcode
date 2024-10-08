class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.queue=[]
        self.size=size
        

    def next(self, val) :
        """
        :type val: int
        :rtype: float
        """
        if self.size==len(self.queue):
            self.queue.pop(0)
        self.queue.append(val)
        
        return float(sum(self.queue))/len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)