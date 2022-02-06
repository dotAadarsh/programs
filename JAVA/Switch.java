//Use the switch statement to select one of many code blocks to be executed.

public class Switch {
    public static void main(String[] args) {
        int choose_artist = 3;
        switch(choose_artist) {

            case 1: 
            System.out.println("Ed sheeran");
            break;   //The break Keyword - When Java reaches a break keyword, it breaks out of the switch block

            case 2: 
            System.out.println("Taylor Swift");
            break;

            case 3: 
            System.out.println("Olivia Rodrigo");
            break;

            case 4: 
            System.out.println("Charlie Puth");
            break;

            case 5: 
            System.out.println("Selena Gomez");
            break;
            
            //The default keyword specifies some code to run if there is no case match
            default: 
            System.out.println("Can't find your artist");

        }

    }
}