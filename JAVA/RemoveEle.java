// Remove Given Character From String

public class RemoveEle {
     public static void main(String[] args) {
        String str = "MMMMMMMMMMMM";
        char c = 'M';
        str = removeChar(str, c);
        System.out.println(str);
    }

    public static String removeChar(String str, char c) {
        if(str.length()==0)
        return "";
        if(str.charAt(0)==c)
        return removeChar(str.substring(1),c);
        return str.charAt(0) + removeChar(str.substring(1), c);

    }
}
