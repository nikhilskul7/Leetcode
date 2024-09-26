class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        
        
        for i in range(len(heights)-1):
            temp=heights[i+1]-heights[i]
            
            if temp<=0:
                continue
                
            bricks-=temp
            heapq.heappush(heap,-temp)
            
            if bricks<0:
                if ladders==0:
                    return i
                bricks-=heapq.heappop(heap)
                ladders-=1
                
        return len(heights)-1