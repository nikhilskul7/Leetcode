class MyCalendar:

    def __init__(self):
        self.bookings=[]

    def book(self, start: int, end: int) -> bool:
        if not self.bookings:
            self.bookings.append([start,end])
            return True

                
        left=0
        right=len(self.bookings)-1
        mid=0
        while left<=right:
            
            mid=(left+right)//2
            
            if self.bookings[mid][1]<=start:
                left=mid+1
                
            elif self.bookings[mid][0]>=end:
                right=mid-1
            else:
                return False
        self.bookings.insert(left,[start,end])
        return True
                
            
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)