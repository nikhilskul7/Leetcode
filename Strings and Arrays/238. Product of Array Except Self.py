class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)

        pre=[1 for _ in range(n)]
        pre[0]=nums[0]
        for i in range(1,n):

            pre[i]=pre[i-1]*nums[i]

        pos=[1 for _ in range(n)]
        pos[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):

            pos[i]=pos[i+1]*nums[i]

        retval=[1 for _ in range(n)]

        retval[0]=pos[1]
        retval[n-1]=pre[n-2]



        for i in range (1,n-1):
            retval[i]=pre[i-1]*pos[i+1]

        return retval