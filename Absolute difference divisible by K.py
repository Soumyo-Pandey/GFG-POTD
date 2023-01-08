class Solution:
    def countPairs (self, n, arr, k):
        # code here
        
        arr.sort()
        my_d = {0:1}
        d = 0
        c_to = 0
        for i in range(1,n):
            d+=abs(arr[i]-arr[i-1])
            if d%k not in my_d:
                my_d[d%k]=1
            else:
                my_d[d%k]+=1
        c_to = 0
        for i in my_d:
            c_t = my_d[i]
            c_to+=(c_t*(c_t-1))//2
        return c_to
