import java.util.ArrayList;
import java.util.function.Consumer;

public class LambdaJava {
    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        numbers.add(10);
        numbers.add(20);
        numbers.add(30);
        numbers.add(40);

        numbers.forEach((n) -> {System.out.println(n);});

        // Lambda expressions can be stored in variables if the variable's type is an interface which has only one method.

        Consumer<Integer> method = (n) -> {System.out.println(n);};
        numbers.forEach(method);
    
    }    
}
