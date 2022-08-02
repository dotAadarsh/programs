public class Example9 {
    static int factorial(int n) {
        if(n<0)
        return -1;
        else if(n==0)
        return 1;
        else
        return n*factorial(n-1);
    }

    public static void main(String[] args) {
        int n = 10;
        System.out.println(factorial(n));
    }
}

// This is just a straight recursion from n to n -1 to n - 2 down to 1. It will take O ( n) time