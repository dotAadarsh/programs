import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegexJava {
    public static void main(String[] args) {
        Pattern pattern = Pattern.compile("Olivia", Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher("Sour by Olivia");
        boolean matchfound = matcher.find();
        if(matchfound)
        System.out.println("Match found");
        else
        System.out.println("Match Not found");

        //The Matcher class also provides appendReplacement and appendTail methods for text replacement.
        
        String REGEX = "a*b";
        String INPUT = "aabfooaabfooabfoob";    
        String REPLACE = "-";

        Pattern p = Pattern.compile(REGEX);
        Matcher m = p.matcher(INPUT);

        StringBuffer sb = new StringBuffer();
        while(m.find()) {
            m.appendReplacement(sb, REPLACE);
        }
        m.appendTail(sb);
        System.out.println(sb.toString());

    }
    

}
