class Solution:
    #Function to find first node if the linked list has a loop.
    def findFirstNode(self, head):
        #code here
        
        sl = head
        fa = head
        temp = head
        
        if(head is None or head.next is None):
            return -1
            
        while(fa.next is not None and fa.next.next is not None):
            sl = sl.next
            fa = fa.next.next
            if(fa == sl):
                while(sl!=temp):
                    sl = sl.next
                    temp = temp.next
                return temp.data
        return -1

