// Reverse of a given integer 

import java.util.Scanner;

public class ReverseNum {
    public static void main(String [] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter the Num: ");
            int num = sc.nextInt();
            System.out.println("The reverse of the number is: ");
            int rev = 0, i=0, c=0;
            while(num!=0) {
                rev = (rev*10) + num%10;
                if(num%10 ==0 && i==0)
                c++;
                else
                i++;
                num/=10;
            }
            for(i=0;i<c;i++)
            System.out.print("0");
            System.out.println(rev);
        }
    }
    

}
