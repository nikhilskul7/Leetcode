"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        pVals = set()
        def traverse_up(root):
            if root == None or root in pVals:
                return root
            pVals.add(root)
            return traverse_up(root.parent)
            
        return traverse_up(p) or traverse_up(q)