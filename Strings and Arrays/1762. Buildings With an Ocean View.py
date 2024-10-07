class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        retval=[]
        stack=[]
        i=0
        while i <len(heights):
            if not stack:
                stack.append((i,heights[i]))
                i+=1
                continue
            
            while stack and stack[-1][1]<=heights[i]:
                    stack.pop()
            stack.append((i,heights[i]))


            i+=1

        for i in stack:
            retval.append(i[0])

        return sorted(retval)
    

or
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        max_height = 0
        
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                result.append(i)
                max_height = heights[i]
        
        return result[::-1]