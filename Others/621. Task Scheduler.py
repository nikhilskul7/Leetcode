class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''count=Counter(tasks)
        retval=0
        hp=[-q for q in count.values()]

        heapq.heapify(hp)

        q=deque()

        while q or hp:
            retval+=1

            if hp:
                cnt=1+heapq.heappop(hp)
                if cnt:
                    q.append([cnt,retval+n])

            if q and q[0][1]==retval :
                heapq.heappush(hp,q.popleft()[0])

        return retval'''

        retval=0
        ct=Counter(tasks)
        
        hp=[-val for val in ct.values()]
        
        heapq.heapify(hp)
        
        q=[]
        
        
        while hp or q:
            retval+=1
            
            if hp:
                temp=heapq.heappop(hp)+1
                
                
                if temp:
                    q.append([temp,retval+n])
            
            if q and q[0][1]==retval:
                heapq.heappush(hp,q.pop(0)[0])

        return retval