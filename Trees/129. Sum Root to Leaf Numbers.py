# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.retval=0
        
        
        def dfs(root,ans):
            if not root:
                return
            
            if not root.left and not root.right:

                self.retval+= ans*10 +root.val
                
                return
            dfs(root.left,ans*10 +root.val)
            dfs(root.right,ans*10 +root.val)  
            
        
        dfs(root,0)
        return self.retval