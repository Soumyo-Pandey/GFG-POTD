class Solution():
    def solve(self, N, A):
        #your code here
        c = 0
        for i in range(N-1, -1, -1):
            if A[i] < 9:
                c = i
                break
            else:
                continue
        return c+1
