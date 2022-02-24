enum Level {
    Low,
    Medium,
    High
}


public class Enum {
    public static void main(String[] args) {
        Level myvar = Level.High;
        switch(myvar) {
            case Low: 
            System.out.println("Low Level");
            break;
            case Medium: 
            System.out.println("Medium Level");
            break;
            case High: 
            System.out.println("High Level");
            break;
        }
    }
}
