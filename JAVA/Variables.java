

public class Variables {
    public static void main(String[] args) {

        String name = "MADMAX";
        int num = 10;
        float floatnum = 1.56f;
        char letter = 'z';
        boolean bool = false;    
        
        /*- Format specifiers begin with a percent character (%) and terminate with a “type character
          - java string format() method returns the formatted string by given locale, format and arguments*/

        System.out.println(String.format("%s %d %f %c %b", name, num, floatnum, letter, bool)); 
        
        //if you assign a new value to an existing variable, it will overwrite the previous value

        int num1 = 10;
        num1 = 20;
        System.out.println(num1);

        //use final keyword if you don't want others (or yourself) to overwrite existing values

        final int num2 = 20;
        // num2 = 40; // will generate an error: cannot assign a value to a final variable
        System.out.println(num2);

        //You can also use the + character to add a variable to another variable

        String first_name = "MAD";
        String last_name = "MAX";
        String full_name = first_name+last_name;
        System.out.println(full_name);

    }
}