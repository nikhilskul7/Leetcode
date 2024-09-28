class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        retval=head
       
        while head and head.next:
            temp=ListNode(gcd(head.val,head.next.val),head.next)
            
            head.next=temp
            head=temp.next
           
        
        
        return retval