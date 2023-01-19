class Solution:
    def carpetBox(self, A,B,C,D):
        #code here
        
        if A>B:
            A,B `= B,A
        if C>D:
            C,D = D,C
        c = 0
        while A>C or B>D:
            if A>C and B>D:
                B = B// 2
            elif A>C:
                A = A//2
            else:
                B = B//2
            if A > B:
                A,B = B,A
            c = c+1
        return c
        
