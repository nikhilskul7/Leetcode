# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            retval=[]
            
            if not root:
                return []
            q=[]
            q.append(root)
           
            while q:
                
                n=len(q)
                t=[]
                
                for i in range(n):
                    temp=q.pop(0)
                    t.append(temp.val)
                    
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
                        
                retval.append(t)
                
                
                
            return retval