# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        
        
        while (len(lists))>1:
            
            mergedList=[]
            
            for i in range(0,len(lists),2):
                
                list1=lists[i]
                list2=lists[i+1] if i+1 <len(lists) else None
                
                mergedList.append(self.mergeTwoLists(list1,list2))
                
            lists=mergedList
            
        return lists[0]
    
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        retval=ListNode()
        dummy=ListNode()
        dummy=retval
        
        while list1 and list2:
            if list1.val > list2.val:
                retval.next=ListNode(list2.val)
                list2=list2.next
            else: 
                retval.next=ListNode(list1.val)
                list1=list1.next
            retval=retval.next
            
        if  list1:
            retval.next=list1
        elif  list2:
            retval.next=list2
        return dummy.next
    