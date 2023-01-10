class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def toSumTree(self, root) :
        #code here
        
        self.solve(root)
    def solve(self,r):
        if r is None:
            return 0
        oldv = r.data
        r.data = self.solve(r.left)+self.solve(r.right)
        
        
        return oldv + r.data
