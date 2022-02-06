//A method is a block of code which only runs when it is called.

public class Methods {
    static void myMethod() {
        System.out.println("It's called");
    }

    public static void main(String[] args) {
        myMethod();
        //you can call it multiple times
        myMethod();
    }
}
