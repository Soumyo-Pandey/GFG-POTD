import bisect
class Solution:
    def minimizeSum(self, N, arr):
        # Code here
        
        arr.sort()
        i=0
        s1 = 0
        while i<N-1:
            if i==0:
                s1+=arr[i]+arr[i+1]
                arr[i+1]=s1
                i+=1
            elif arr[i]<=arr[i+1]:
                s1=s1+(arr[i]+arr[i+1])
                arr[i+1]=(arr[i]+arr[i+1])
                i+=1
            else:
                v=arr.pop(i)
                bisect.insort(arr,v)
        return s1
