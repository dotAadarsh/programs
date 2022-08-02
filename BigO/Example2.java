// The inner for loop has O(N) iterations and it is called N times. Therefore, the runtime is O(N2)

public class Example2 {
    
    public static void foo(int[] arr) {
        for(int i = 0;i<arr.length;i++) {
            for(int j=0;j<arr.length;j++) {
                System.out.println(arr[i] + "," + arr[j]);
            }
        }
    }
    
    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5};
        foo(arr);
    
    }
}