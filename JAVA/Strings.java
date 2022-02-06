//Strings are used for storing text.

public class Strings {
    public static void main(String[] args) {

        //Create a variable of type String and assign it a value
        String monday = "morning";
        System.out.println(monday);

        //A String in Java is actually an object, which contain methods that can perform certain operations on strings.
        //the length of a string - length() method
        String series = "Rick and Morty";
        System.out.println("The length of the string is: " + series.length());

        //To uppercase letters - toUpperCase()
        System.out.println(series.toUpperCase());

        //To lowercase letters - toLowerCase()
        System.out.println(series.toLowerCase());

        //indexOf() method returns the index (the position) of the first occurrence of a specified text in a string (including whitespace)
        System.out.println(series.indexOf("and"));

        //Concatenation - +  is used to combine
        String com = "Concati";
        String bine = "nation";
        String combine = com+bine;
        System.out.println(combine);
        //You can also use the concat() method to concatenate two strings
        System.out.println(com.concat(bine));

        //Because strings must be written within quotes, Java will misunderstand this string, and generate an error:
        //String sentence = "Sour album by "Olivia rodrigo" is out now"
        //The solution to avoid this problem, is to use the backslash escape character.

        // \" - inserts double quotes, \' - inserts single quotes, \\ - Backslash
        String lyrics = "You walked in \"my life\" at 2am\\... \'I never fall in love\'";
        System.out.println(lyrics);

        // \n - new line, \b  backspace, \r - carriage return, \f - form feed, \t - tab
        String song = "I dont want to get \t separated a\b \nI wanna stay with you";
        System.out.println(song);

        //Let's get deeper

        String company = "Spotify";
        System.out.println(company.charAt(4)); //charAt() Method - Return the first character (0)
        System.out.println(company.codePointAt(4)); //codePointAt() Method - Return the Unicode
        System.out.println(company.codePointBefore(4)); //codePointBefore() Method  returns the Unicode value of the character before the specified index
        System.out.println(company.codePointCount(1,5)); //codePointCount()	Method - returns the number of Unicode values

        String artist = "Olivia";
        System.out.println(company.compareTo(artist)); //compareTo() Method - compares two strings lexicographically

        String myfav = "Drivers lIcense";
        String mylove = "dRiVeRs LICense";
        System.out.println(myfav.compareToIgnoreCase(mylove)); //compareToIgnoreCase() Method - compares two strings lexicographically, ignoring lower case and upper case differences
        System.out.println(myfav.concat(artist)); //concat() Method - appends (concatenate) a string to the end of another string
        System.out.println(artist.contains("liv")); //contains() Method - checks whether a string contains a sequence of characters
        System.out.println(company.contentEquals("Spotify")); //contentEquals() Method - searches a string to find out if it contains the exact same sequence of characters in the specified string or StringBuffer
        
        char[] playlist = {'C', 'H', 'I', 'L', 'L'};
        String playlist_name = "";
        playlist_name = playlist_name.copyValueOf(playlist,0,5); //copyValueOf() Method - returns a String that represents the characters of a char array
        System.out.println("Returned playlist is: " + playlist_name);

        System.out.println(mylove.endsWith("ese")); //endsWith() Method - checks whether a string ends with the specified character(s).
        System.out.println(myfav.equals(mylove)); //equals() Method - compares two strings, and returns true if the strings are equal, and false if not

        /*String equals() VS contentEquals(): The equals() method is to compare the contents of two Strings are same whereas contentEquals method is to compare String with StringBuffer or StringBuilder. 
        But both are to compare the contents. In other words, contentEquals method does equals() method + additional comparison with StringBuffer, StringBuilder, etc./
        */

        System.out.println(mylove.equalsIgnoreCase(myfav)); //equalsIgnoreCase() Method - compares two strings, ignoring lower case and upper case differences
        System.out.println(String.format("%s", myfav)); //format() - Returns a formatted string using the specified locale, format string, and arguments	

        byte byte_var[] = company.getBytes(); //getBytes() Method - Encodes this String into a sequence of bytes using the named charset, storing the result into a new byte array
        for(int i=0;i<byte_var.length;i++){
            System.out.println(byte_var[i]);
        }
        
        char[] ch = new char[10];
        company.getChars(1,6,ch,0); //getChars() Method - copies the content of this string into a specified char array
        System.out.println(ch);

        System.out.println(mylove.hashCode()); //hashCode() method returns the hash code of a string
        
        String phrase = "All these voices in my head get loud. I wish I could shut them out";
        System.out.println(phrase.indexOf("head")); //indexOf() Method - returns the position of the first occurrence of specified character(s) in a string
        System.out.println(phrase.indexOf("e", 9));
        System.out.println(phrase.indexOf(65));
        System.out.println(phrase.indexOf(101, 9));
        
        String podcast1 = new String("Lazarus Heist");
        String podcast2 = new String("Lazarus Heist");
        System.out.println(podcast1 == podcast2); //Returns false
        /*The println statement prints false because separate memory is allocated for each string literal. 
        Thus, two new string objects are created in the memory i.e. str and str1. that holds different references.
        So intern() is used to overcome this*/

        String genre1 = new String("pop sauce").intern(); //intern() Method - Returns the canonical representation for the string object	
        String genre2 = new String("pop sauce").intern();
        System.out.println(genre1==genre2);

        String test="";
        System.out.println(test.isEmpty()); //isEmpty() Method - checks whether a string is empty or not
        System.out.println(company.isEmpty());

        System.out.println(phrase.lastIndexOf("I")); //lastIndexOf() Method - returns the position of the last occurrence of specified character(s) in a string
        System.out.println(phrase.length()); //length() Method - returns the length of a specified string

        /* Regular Expression - https://regex101.com/ 
        Regex is an API to define a pattern for searching or manipulating strings.*/

        System.out.println(phrase.matches("(.*)voices in my(.*)")); //matches() Method - tells whether or not this string matches the given regular expression
        System.out.println(phrase.regionMatches(10,"voices",0,5)); //regionMatches() Method - has two variants that can be used to test if two string regions are equal
        System.out.println(phrase.regionMatches(true,10,"VoiCeS",0,5));//regionMatches() Method - With ignoreCase has two variants that can be used to test if two string regions are equal. 

        System.out.println(podcast1.replace('L', 'H')); //replace() Method - searches a string for a specified character, and returns a new string where the specified character(s) are replaced
        System.out.println(genre1.replaceFirst("[s]", "l")); //replaceFirst() Method - Replaces the first occurrence of a substring that matches the given regular expression with the given replacement
        System.out.println(genre1.replaceAll("[p]","l")); //replaceAll() Method - Replaces each substring of this string that matches the given regular expression with the given replacement
        
        String[] words = phrase.split("\\s"); //split() Method - splits this string against given regular expression and returns a char array
        for(String w:words){
            System.out.println(w);
            }

        System.out.println(phrase.startsWith("A")); //startsWith() Method - checks whether a string starts with the specified character(s)
        System.out.println(podcast1.substring(8)); //substring() Method - Returns a new string which is the substring of a specified string
        
        char[] ch_artist = artist.toCharArray(); //toCharArray() Method - Converts the string to a new character array
        for(int i=0;i<ch_artist.length;i++){
            System.out.println(ch_artist[i]);
        }

        String live = "   Without You   "; 
        System.out.println(live.trim()); //trim() Method - Remove whitespace from both sides of a string
        
        int listeners = 10009090;
        String worldwide = String.valueOf(listeners); //valueOf() Method - Returns the string representation of the specified value
        System.out.println(worldwide);
    
    }
}
