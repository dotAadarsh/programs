// Recursion is the technique of making a function call itself

public class Recursion {
    
    //Use recursion to add all of the numbers up to 10.

    public static int sum(int val) {
        if(val>0) {
            return(val + sum(val-1));
        }
        else {
            return 0;
        }
    }

    //Halting condition
    //Use recursion to add all of the numbers between 5 to 10

    public static int sum(int start, int end) {
        if(end>start) {
            return(end + sum(start, end-1));
        }
        else {
            return 0;
        }
    }

    public static void main(String[] args) {
        int result = sum(15);
        System.out.println(result);
        int result_btw = sum(5,10);
        System.out.println(result_btw);
    }
}
