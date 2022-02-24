import java.util.HashMap;

public class Hashmap {
    public static void main(String[] args) {
        HashMap<String, String> album = new HashMap<String, String>();
        album.put("Divide", "Ed Sheeran");
        album.put("Sour", "Olivia Rodrigo");
        album.put("Music to be murdered by", "Eminem");

        System.out.println(album);

        // Access an Item
        System.out.println(album.get("Divide"));

        // Remove an Item
        album.remove("Sour");
        System.out.println(album);

        // HashMap Size
        System.out.println(album.size());

        // Print keys
        for(String i : album.keySet())
        {
            System.out.println(i);
        }

    }
}
