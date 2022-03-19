// Java program to rotate an array by d elements
import java.util.Scanner;

public class RotateArray {

    void leftRotate(int arr[], int d, int n) {
        for(int i=0;i<d;i++) {
            leftRotatebyone(arr, n)
;        }
    }
    
    void leftRotatebyone(int arr[], int n) {
        int i, temp;
        temp = arr[0];
        for(i=0;i<n-1;i++) {
            arr[i] = arr[i+1];
        }
        arr[n-1] = temp;
    }

    void printRotate(int arr[], int n) {
        System.out.println("The rotated Array is ");
        for(int i=0;i<n;i++) {
            System.out.println(arr[i] + " ");
        }
    }
public static void main(String[] argc) {
    int []arr = new int[10];
    int n,d;

    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the number of elements in the array");
    n=sc.nextInt();
    
    for(int i=0;i<n;i++) {
        arr[i] = sc.nextInt();
    }
    System.out.println("Enter the num of elemets to be rotated");
    d=sc.nextInt();

    RotateArray rotate = new RotateArray();
    rotate.leftRotate(arr,d,n);
    rotate.printRotate(arr,n);

}
}

//Time complexity : O(n * d) 
//Auxiliary Space : O(1)