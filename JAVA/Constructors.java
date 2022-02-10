/*A constructor in Java is a special method that is used to initialize objects. 
The constructor is called when an object of a class is created. 
It can be used to set initial values for object attributes*/

public class Constructors {

    int x; //Create a class attribute
    int y;

    public Constructors(int z) {
        
        x=5; // Set the initial value for the class attribute x
        y=z; //Constructors can also take parameters, which is used to initialize attributes.

    }

    public static void main(String[] args) {
        Constructors myobj = new Constructors(10); // Create an object of class Main (This will call the constructor)
        System.out.println(myobj.x);
        System.out.println(myobj.y);
    }
    
}
