//The while loop loops through a block of code as long as a specified condition is true:

public class While {
    public static void main(String[] args) {
        int gas = 7;
        while(gas<10) {
            System.out.println("Not empty");
            gas++;
        }

        //The do/while loop is a variant of the while loop. This loop will execute the code block once, before checking if the condition is true, then it will repeat the loop as long as the condition is true.

        int num = 7;
        do {
            System.out.println("Do is executed");
            num++;
        }
        while(num<10);

    }
    
}
