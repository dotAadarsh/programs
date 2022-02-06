

public class TypeCasting {
    public static void main(String[] args) {
        //Widening Casting
        int wideint = 10;
        double widedouble = wideint; //Automatic casting: int to double
        System.out.println(wideint);
        System.out.println(widedouble);

        //Narrowing Casting
        double narrowdouble = 9.34d;
        int narrowint = (int) narrowdouble; //Manual casting: double to int
        System.out.println(narrowdouble);
        System.out.println(narrowint);

    }
}