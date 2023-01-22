class Solution {
    public static int solve(int N, int k, int[] arr) {
        // code here
        
        if(N==1) return arr[0];
        int a = 1;
        for(int i=1; i<N; i++){
            arr[i]+=arr[i-1];
        }
        if(k==1) return arr[N-1];
        for(int i=2; i*i<=arr[N-1]; i++){
            if(arr[N-1]%i==0){
                int c=0, d=0, z=arr[N-1]/i;
                for(int j : arr){
                    if(j%i==0) c++;
                    if(j%z==0) d++;
                }
                
                if(c>=k) a=Math.max(a,i);
                if(d>=k) a=Math.max(a,z);
            }
        }
        return a;
    }
}
