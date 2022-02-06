/*Use if to specify a block of code to be executed, if a specified condition is true
Use else to specify a block of code to be executed, if the same condition is false
Use else if to specify a new condition to test, if the first condition is false
Use switch to specify many alternative blocks of code to be executed*/

public class IfElse {

    public static void main(String[] args) {
        if(3.14>2.14) {
            System.out.println("Yep, it's greater");
        }

        int played = 47;
        if(played == 50) {
            System.out.println("Wow! you have listened it 50 times");
        }
        else {
            System.out.println("keep listening");
        }


    String song = "perfect"; 
    if(song == "we dont talk anymore") {
        System.out.println("by Charlie Puth ft.Selena Gomez");
    }
    else if(song == "perfect") {
        System.out.println(song +" by Ed Sheeran");
    }
    else {
        System.out.println("by Unknown artist");
    }

    String time = "AM";
    String remix = (time == "AM") ? "Morning Remix" : "Evening Remix";
    System.out.println(remix);
}
}
