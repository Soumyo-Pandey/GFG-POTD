class Solution():
    def m(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        head = Node(-1)
        t=head
        while l1!=None and l2!=None:
            if l1.data<=l2.data:
                t.bottom = l1
                l1=l1.bottom
            else:
                t.bottom=l2
                l2=l2.bottom
            t=t.bottom
        if l1!=None:
            t.bottom=l1
        if l2!=None:
            t.bottom=l2
        return head.bottom
    
    def flatten(self,root):
        #Your code here
        while root.next!=None:
            a=root
            b=root.next
            c=root.next.next
            root=self.m(a,b)
            root.next=c
        return root
