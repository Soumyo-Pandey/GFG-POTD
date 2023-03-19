from typing import List


class Solution:
    def getDistinctDifference(self, N : int, A : List[int]) -> List[int]:
        # code here
        
        le = [0]*N
        ri = [0]*N
        
        z = []
        
        s1 = set()
        s2 = set()
        
        for i in range(N):
            le[i] = len(s1)
            s1.add(A[i])
            
        for i in range(N-1, -1, -1):
            
            ri[i] = len(s2)
            s2.add(A[i])
            
        for i in range(N):
            z.append(le[i]-ri[i])
            
        return z
