class Solution:
    def minIncrements(self, arr, N): 
        # Code here
        
        arr.sort()
        z=sum(arr)
        for i in range(1,N):
            if arr[i]<=arr[i-1]:
                arr[i]=arr[i-1]+1
        return sum(arr)-z
