# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.retval=None
        
        
        def check(root):
            if not root or root==p or root==q:
                return root
            
            lh=check(root.left)
            rh=check(root.right)
           
            if not lh:
                return rh
            elif not rh:
                return lh
            else:
                return root
        
        
        return check(root)
        
                