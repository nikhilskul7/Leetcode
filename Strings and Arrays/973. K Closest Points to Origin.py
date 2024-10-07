class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        
        for x,y in points:
            temp=pow(x,2)+pow(y,2)
            
            minheap.append((temp,[x,y]))
        
        heapq.heapify(minheap)
        return [heapq.heappop(minheap)[1] for _ in range(k)]