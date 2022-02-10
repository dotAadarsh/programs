//Example for Accessing Methods With an Object

public class AccessMethod {
    public void Album() {
        System.out.println("The album is Divide");
    }

    public void Songs(int total) {
        System.out.println("has " + total +" songs");
    }

    public void Artist() {
        System.out.println("Composed by Ed Sheeran");
    }

    public static void main(String[] args) {
        AccessMethod obj = new AccessMethod();
        obj.Album();
        obj.Songs(15);
        obj.Artist(); 
    }
}
