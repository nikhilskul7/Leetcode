# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        
        def check(root):
            
            if not root:
                return -1
            
            lh=check(root.left)
            rh=check(root.right)
        
            self.ans=max(self.ans,2+lh+rh)
            return 1+max(lh,rh)
        check(root)
        return self.ans