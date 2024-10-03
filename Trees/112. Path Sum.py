# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        sumi=0
        
        def check(cur,sumi):
            if not cur:
                return False
            sumi+=cur.val
            
            
            if sumi==targetSum and ( not cur.left and not cur.right):
                return True
            
            
            
            l=False
            r=False
            
            if cur.left:
                l=check(cur.left,sumi)
            if cur.right:
                r=check(cur.right,sumi)
            
            return l or r
        
        return check(root,sumi)