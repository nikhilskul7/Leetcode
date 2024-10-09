# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balance(root,ht):
            if not root:
                return 0
            
            l=balance(root.left,ht+1)
            r=balance(root.right,ht+1)
            if l==-1 or r==-1:
                return -1
            if abs(l-r)>1:
                return -1
            return 1+max(l,r)
          
            
        if balance(root,0)!=-1:
            return True
        return False