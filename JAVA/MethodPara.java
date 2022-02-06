//Information can be passed to methods as parameter. Parameters act as variables inside the method.

public class MethodPara {

    static void artist(String name) {
        System.out.println("The artist is " + name);
    }

    //multiple parameter
    static void artist_detail(String name, int age, long listeners) {
        System.out.println("The artist is " + name + " whose age is " + age + " has monthly listeners of " + listeners);
    }

    //Return Values
    static String app(String app_name) {
        return ("My fav app is " + app_name);
    }

    //Method with If...Else
    static void access(boolean subscription) {
        if(subscription==true) {
            System.out.println("Ad free music");
        }
        else {
            System.out.println("Arey yaar");
        }
    }

    //Method Overloading
    //With method overloading, multiple methods can have the same name with different parameters
    static int votes(int likes, int dislikes) {
        return likes-dislikes;
    }

    static double votes(double likes, double dislikes) {
        return likes-dislikes;
    }

    public static void main(String args[]) {
        artist("Olivia"); //When a parameter is passed to the method, it is called an argument
        artist_detail("Olivia", 18, 193942345); //You can have as many parameters as you like
        System.out.println(app("Spotify")); //return type
        access(false);
        int int_votes = votes(787,434);
        double double_votes = votes(44423423,55343424);
        System.out.println("int: " + int_votes);
        System.out.println("double: " + double_votes);
    }

}
