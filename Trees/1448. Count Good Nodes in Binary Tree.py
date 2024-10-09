# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        retval=[]
        def dfs(root,num):
            if not root:
                return
            if root.val>=num:
                retval.append(root.val)
            
            dfs(root.left,max(num,root.val))
            dfs(root.right,max(num,root.val))
            
        dfs(root,float('-inf'))
        
        return len(retval)