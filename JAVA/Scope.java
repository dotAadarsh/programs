// In Java, variables are only accessible inside the region they are created. This is called scope.

public class Scope {
    
    public static void main(String[] args) {
        
        //Method Scope
        // Code here CANNOT use x
        int x = 100;
        // Code here can use x
        System.out.println(x);
        { // This is a block

        // Code here CANNOT use y
        int y = 100;

        // Code here CAN use y
        System.out.println(y);
  
     } // The block ends here
    
    }
}
