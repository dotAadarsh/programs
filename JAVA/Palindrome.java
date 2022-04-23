public class Palindrome {

    public static void main(String[] args) {
        System.out.println("is aaa palindrome? " + isPalindrom("aaa"));
    }

    public static boolean isPalindrom(String text) {
        String reverse = reverse(text);
        if(text.equals(reverse))
        return true;
        else 
        return false;
    }

    public static String reverse(String input) {
        if(input==null || input.isEmpty()){
            return input;
        }
        return input.charAt(input.length()-1) + reverse(input.substring(0,input.length()-1));
    }

}


