class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        retval=0
        
        stack=[]
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>=h:
                id,ht=stack.pop()
                start=id
                retval=max(retval,(i-id)*ht)
            stack.append((start,h))
        for i,h in stack:
            retval=max(retval,(len(heights)-i)*h)
        return retval