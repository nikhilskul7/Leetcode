# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.retval=('inf')
        self.closest=root.val
        def check(root):
            if not root:
                return
            if self.retval>abs(root.val-target):
              
                self.retval=abs(root.val-target)
                self.closest=root.val
            if self.retval==abs(root.val-target):
                if self.closest>root.val:
                
                    self.closest=root.val
            if target>root.val:
                check(root.right)
            else:
                check(root.left)

        check(root)

        return self.closest
        