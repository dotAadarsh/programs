//When you know exactly how many times you want to loop through a block of code, use the for loop instead of a while loop

public class ForLoop {
    public static void main(String [] args) {

        int queue = 5;
        for(int i=0; i < queue; i++)
        {
            System.out.println((queue-i) + " - Songs left in the queue");
        }

        //a "for-each" loop, which is used exclusively to loop through elements in an array

        String[] songs = {"Heat Waves", "Counting stars", "Believer", "Heathens"};
        for(String i : songs) {
            System.out.println(i);
        }
    }
}
