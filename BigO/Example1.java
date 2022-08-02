public class Example1 {
                          
    public static void foo(int[] arr) {
        int sum = 0;
        int product = 1;
    
        for(int i=0;i<arr.length; i++) {
            sum += arr[i];
        }
    
        for(int i=0;i<arr.length; i++) {
            product *= arr[i];
        }
    
        System.out.println(sum + " " + product);
    }
    
    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5};
        foo(arr);
    
    }
}
