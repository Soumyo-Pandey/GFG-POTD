class Solution():
    def maxWeightCell(self, N, Edge):
        #your code goes here
        wei = [0]*N
        for i in range(N):
            if Edge[i] != -1:
                wei[Edge[i]] += i
                
        mx = max(wei)
        return[i for i,n in enumerate(wei) if n==mx][-1]
