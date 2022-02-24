public class ThrowJava {

    static void checkage(int age) {
        if(age<18) {
            throw new ArithmeticException("Access Denies - You must be at least 18 years old.");
        }
        else {
            System.out.println("Access granted - You are old enough!");
        }
    }
    public static void main(String[] args) {
        checkage(14);
        checkage(19);
}
}

