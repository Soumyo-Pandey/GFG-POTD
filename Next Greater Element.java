class Solution{
    public static long[] nextLargerElement(long[] arr, int n) { 
        // Your code here
        
        long [] a = new long[n];
        Stack<Long>stack = new Stack<>();
        a[n-1] = -1;
        stack.push(arr[n-1]);
        for(int i=n-2; i>=0; i--)
        {
            while(!stack.isEmpty() && stack.peek() <= arr[i]){
                stack.pop();
            }
            if(stack.size()==0)a[i] = -1;
            else a[i] = stack.peek();
            stack.push(arr[i]);
        }
        return a;
    } 
}
