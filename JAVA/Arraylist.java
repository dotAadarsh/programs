import java.util.ArrayList;
import java.util.Collections; //// Import the Collections class

public class Arraylist {
  public static void main(String[] args) {

    ArrayList<String> songs = new ArrayList<String>();
    songs.add("Brutal");
    songs.add("Deja Vu");
    songs.add("Drivers License");
    System.out.println(songs);
    System.out.println(songs.get(2)); // Access an Item
    songs.set(0, "Happier"); // Change an Item
    System.out.println(songs);
    System.out.println(songs.size()); // ArrayList Size
    songs.clear(); // remove all the elements 
    System.out.println(songs);

    // loop through an ArrayList with the for-each loop
    songs.add("Shivers");
    songs.add("Bad Habits");
    songs.add("Perfect");
    songs.add("Shape of you");
    for(String i : songs) {
      System.out.println(i);
    }

    //Sort an ArrayList
    System.out.println("sort() method for sorting lists alphabetically or numerically");
    Collections.sort(songs);
    for(String i : songs)
    System.out.println(i);

   }
}