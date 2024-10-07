"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm={None:None}
        cur=head
        
        
        while cur:
            temp=Node(cur.val)
            hm[cur]=temp
            cur=cur.next
        
        cur=head
        
        while cur:
            temp=hm[cur]
            temp.next=hm[cur.next]
            temp.random=hm[cur.random]
            cur=cur.next
        return hm[head]