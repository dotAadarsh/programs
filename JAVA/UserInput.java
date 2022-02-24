import java.util.Scanner;

public class UserInput {
    public static void main(String[] args) {
        Scanner myobj = new Scanner(System.in);

        System.out.println("enter the artist name");
        String artistname =  myobj.nextLine();
        System.out.println("Enter the number of songs");
        int songs = myobj.nextInt();
        System.out.println(artistname + "Has writtern " + songs + "songs");
    }
    
}
