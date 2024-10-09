# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if  root==None :
            return False
        if self.checki(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def checki(self,root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if  root1.val !=  root2.val:
                return False
            lh=self.checki(root1.left,root2.left)
            rh=self.checki(root1.right,root2.right)

            return lh and  rh
