//A method is a block of code which only runs when it is called.

public class Methods {

    static void StaticMethod() {
        System.out.println("Static methods can be called without creating objects");
    }

    public void PublicMethod() {
        System.out.println("Public must be called by creating objects");
    }

    public static void main(String[] args) {
        StaticMethod();
        //you can call it multiple times
        StaticMethod();

        Methods myobj = new Methods();
        myobj.PublicMethod();

    }
}
