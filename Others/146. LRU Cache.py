class Node:
    def __init__(self,key:int,value):
        self.key=key
        self.next=None
        self.prev=None
        self.value=value

class LRUCache:

    def __init__(self, capacity: int):
        self.hm={}
        self.capacity=capacity
        
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def deleteNode(self,temp):
        t1=temp.prev
        t2=temp.next
        t1.next=t2
        t2.prev=t1
        
    def addNode(self,temp):
        
            t=self.head.next
            temp.next=t
            t.prev=temp
            temp.prev=self.head
            self.head.next=temp
            
        

    def get(self, key: int) -> int:
        if key in self.hm:
            temp=self.hm[key]
            ans=temp.value
            del self.hm[key]
            self.deleteNode(temp)
            self.addNode(temp)
            self.hm[key]=self.head.next
            
            return ans
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            temp=self.hm[key]
            self.deleteNode(temp)
            del self.hm[key]
            
        if len(self.hm)==self.capacity:
            del self.hm[self.tail.prev.key]
            self.deleteNode(self.tail.prev)
            
            
        
            
        temp=Node(key=key,value=value)
            
        self.addNode(temp)
            
        self.hm[key]=self.head.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)