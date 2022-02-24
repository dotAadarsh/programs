import java.util.ArrayList;
import java.util.Iterator;

public class JavaIterator {
    public static void main(String[] args) {
        ArrayList<String> artist = new ArrayList<String>();
        artist.add("Ed sheeran");
        artist.add("Olivia Rodrigo");
        artist.add("Taylor Swift");

        Iterator<String> it = artist.iterator(); // Get the iterator
        System.out.println(it.next()); // Print the first item

        while(it.hasNext()) {
            System.out.println(it.next());
        }

}
}

