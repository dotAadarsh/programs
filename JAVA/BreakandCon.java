import javafx.scene.control.skin.ContextMenuSkin;

public class BreakandCon {
    public static void main(String[] args) {
        //The break statement can also be used to jump out of a loop.
        for(int i=0;i<5;i++){
            if(i==5)
            break;
            System.out.println(i);
        }

        //continue statement breaks one iteration (in the loop), if a specified condition occurs, and continues with the next iteration in the loop
        for(int i=0; i<5; i++) {
            if(i==3)
            continue;
            System.out.println(i);
        }

        //Break and Continue in While Loop
        int i=0;
        while(i<5) {
            System.out.println(i);
            i++;
            if(i==3){
                break;
            }
        }

        int j=0;
        while(j<5) {
            if(j==2) {
                j++;
                continue;   
            }
            System.out.println(j);
            j++;
        }

    }
}
