# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
            retval=[]
            visit=set()
            
            def check(root,level):
                if not root:
                    return
                if level not in visit:
                    visit.add(level)
                    retval.append(root.val)
                
                check(root.right,level+1)
                check(root.left,level+1)
            
            
            check(root,0)
            return retval