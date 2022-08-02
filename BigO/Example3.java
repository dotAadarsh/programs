// The sum of 1 through N-1 is N(N-1)/2, so the runtime will be O(N2).

public class Example3 {
    
    public static void foo(int[] arr) {
        for(int i = 0;i<arr.length;i++) {
            for(int j=i+1;j<arr.length;j++) {
                System.out.println(arr[i] + "," + arr[j]);
            }
        }
    }
    
    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5};
        foo(arr);
    
    }
}