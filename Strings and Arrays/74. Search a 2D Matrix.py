class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        n=len(matrix)
        m=len(matrix[0])
        high=n*m-1

        while(low<=high):
            mid=(low+high)//2
            val= matrix[mid//m][mid%m]

            if val==target:
                return True
            elif val<target:
                low=mid+1
            else:
                high=mid-1
            
        return False