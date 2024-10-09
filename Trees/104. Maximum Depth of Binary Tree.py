# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dept(root,d):
            if not root:
                return d
            
            l=dept(root.left,d+1)
            r=dept(root.right,d+1)
            
            return max(l,r)
        
        return dept(root,0)