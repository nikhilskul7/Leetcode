class MyCalendarTwo:

    def __init__(self):
        self.nonOverlapBookings=[]
        self.overlapBookings=[]
        

    def book(self, start: int, end: int) -> bool:
        
        for s,e in self.overlapBookings:
            if e>start and end>s:
                return False
        
        for s ,e in self.nonOverlapBookings:
            
            if e>start and end>s:
               
                self.overlapBookings.append([max(s,start),min(e,end)])
                
                
        self.nonOverlapBookings.append([start,end])
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)