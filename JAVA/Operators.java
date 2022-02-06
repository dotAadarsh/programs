//Operators are used to perform operations on variables and values.

public class Operators {
    public static void main(String[] args) {
        
        //Arithmetic Operators
        int x = 56 + 34;
        System.out.println(x);
        int y = 89 - 80;
        System.out.println(x*y);
        System.out.println(x/y);
        System.out.println(x%y);
        System.out.println(++x);
        System.out.println(--y);

        //Assignment Operators
        int a = 10;
        System.out.println(a += 5);
        System.out.println(a -= 3);
        System.out.println(a *= 2);
        System.out.println(a /= 6);
        System.out.println(a %= 2);
        System.out.println(a &= 10);
        System.out.println(a ^= 10);
        System.out.println(a |= 10);
        System.out.println(a >>= 12);
        System.out.println(a <<= 2);

        //Comparison Operators
        int cmp = 25;
        System.out.println(cmp == 25);
        System.out.println(cmp!=20);
        System.out.println(cmp>22);
        System.out.println(cmp<2);
        System.out.println(cmp>=25);
        System.out.println(cmp<=52);

        //Logical Operators
        int lgl = 44;
        System.out.println(lgl<44 && 25>1);
        System.out.println(45<44 || lgl<+4);
        System.out.println(!(lgl>44));

    }
}
     