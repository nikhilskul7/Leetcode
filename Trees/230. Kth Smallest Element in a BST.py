# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''s=[]
        n=0
        
        temp=root
        while s or temp:
            while temp:
                s.append(temp)
                temp=temp.left
            temp=s.pop()
            n+=1
            if n==k:
                return temp.val
            temp=temp.right
            
        '''
        ans=0
        def check(root,n):
            if not root or n >= k:
                returna
            check(root.left,n)
            n+=1
            if n==k:
                print(root)
                ans= root.val
                return
            check(root.right,n)
            
        
        check(root,0)
        return ans
            