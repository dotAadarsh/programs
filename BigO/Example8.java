import java.util.Scanner;

public class Example8 {
    static boolean isPrime(int n) {
        for(int i = 2; i*i <= n;i++) {
            if(n%i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(isPrime(n));
    }
}

// The for loop will start when x = 2 and end when x*x = n. Or, in other words, it stops when x = vn (when x equals the square root of n)
// This runs in O( vn) time. 
