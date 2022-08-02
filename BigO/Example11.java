public class Example11 {
    public static int fibo(int n) {
        if(n<=0) return 0;
        else if (n==1) return 1;
        return fibo(n-1) + fibo(n-2);
    }

    public static void main(String[] args) {
        int n = 10;
        System.out.println(fibo(n));
    }
}

// O( branches^depth) 
// There are 2 branches per call, and we go as deep as N, therefore the runtime is O( 2^N). 