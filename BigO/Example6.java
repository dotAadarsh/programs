public class Example6 {
    
    public static void reverse(int[] arr) {
        for(int i =0;i<arr.length/2; i++) {
            int other = arr.length - i - 1;
            int temp = arr[i];
            arr[i] = arr[other];
            arr[other] = temp;
            }
    }
    
    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5};
        reverse(arr);
        for (int element: arr) {
            System.out.println(element);
        }
    }
}

// This algorithm runs in O ( N) time. The fact that it only goes through half of the array (in terms of iterations) does not impact the big O time