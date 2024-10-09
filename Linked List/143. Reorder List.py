# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            
        prev=None
        cur=slow.next
        
        while cur:
            temp=cur.next
            
            cur.next=prev
            
            prev=cur
            cur=temp
        slow.next=None
        st=head
        mid=prev
        
        while  mid:
            
            stnext=st.next
            midnext=mid.next
            
            st.next=mid
            mid.next=stnext
            
            st=stnext
            mid=midnext
            
            