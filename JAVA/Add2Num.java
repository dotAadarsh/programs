import java.util.Scanner;

public class Add2Num {
    public static void main(String[] args) {
        int x,y,sum;
        Scanner myobj = new Scanner(System.in);
        System.out.println("Enter the two numbers");
        x = myobj.nextInt();
        y = myobj.nextInt();
        sum = x+y;
        System.out.println("The sum is " + sum);
    }
}
