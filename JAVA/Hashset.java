import java.util.HashSet;

public class Hashset {
    public static void main(String[] args) {
        HashSet<String> album = new HashSet<String>();
        album.add("Sour");
        album.add("After Hours");
        album.add("1989(Delux)");
        System.out.println(album);

        // Check If an Item Exists
        album.contains("1989(Delux)");

        for(String i : album) {
            System.out.println(i);
        }

    }
}
