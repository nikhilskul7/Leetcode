# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return root

        queue = deque()
        result = defaultdict(list)
        queue.append((0,root))

        while queue:
            pos,node = queue.popleft()
            result[pos].append(node.val)

            if node.left:
                queue.append((pos-1,node.left))
            if node.right:
                queue.append((pos+1,node.right))

        
        respose =list()

        for key in sorted(result.keys()):
            respose.append(result[key])
        return respose