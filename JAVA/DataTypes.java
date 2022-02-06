
public class DataTypes {

    public static void main(String[] args) {

    //byte - store whole numbers from -128 to 127
    byte byte_num = 101;
    System.out.println(byte_num);

    //short - store whole numbers from -32768 to 32767
    short short_num = 32767;
    System.out.println(short_num);

    //int - store whole numbers from -2147483648 to 2147483647
    int int_num = 34343434;
    System.out.println(int_num);

    //long - store whole numbers from -9223372036854775808 to 9223372036854775807 | Note that you should end the value with an "L"
    long long_num = 12345678912345L;
    System.out.println(long_num);

    //float - store fractional numbers from 3.4e−038 to 3.4e+038 | Note that you should end the value with an "f"
    float float_num = 3.44f;
    System.out.println(float_num);

    //double - store fractional numbers from 1.7e−308 to 1.7e+308 | Note that you should end the value with a "d"
    double double_num = 14.44d;
    System.out.println(double_num);

    //boolean - can only take the values true or false
    boolean bool_value = true;
    System.out.println(bool_value);

    //char - store a single character | must be surrounded by single quotes
    char Gee = 'G';
    System.out.println(Gee);
    //Alternatively, you can use ASCII values to display certain characters
    char var1 = 65;
    System.out.println(var1);

    //String - store a sequence of characters | must be surrounded by double quotes
    String editor = "Gitpod";
    System.out.println(editor);

    }
}
