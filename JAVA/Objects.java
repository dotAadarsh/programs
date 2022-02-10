// Java is an object-oriented programming language. Everything in Java is associated with classes and objects, along with its attributes and methods. For example: in real life, a car is an object. The car has attributes, such as weight and color, and methods, such as drive and brake.
//To create an object of Main, specify the class name, followed by the object name, and use the keyword new:

public class Objects {
    int x = 5;
    final int y = 10;
    String name = "Rick";

    public static void main(String[] args) {
        Objects myobj = new Objects();
        myobj.x = 40; //Modify Attributes - override existing values
        System.out.println(myobj.x);

        //If you don't want the ability to override existing values, declare the attribute as final:
        //  myobj.y = 10;  -  will generate an error: cannot assign a value to a final variable 

        //Multiple attribute
        System.out.println(myobj.name + " with ID number " + myobj.x + " is from Rixty Minute universe");

    } 

}
