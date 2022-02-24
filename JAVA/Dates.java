import java.time.LocalDateTime; // import the LocalDateTime class
import java.time.format.DateTimeFormatter;

public class Dates {
  public static void main(String[] args) {
    LocalDateTime myObj = LocalDateTime.now();
    System.out.println(myObj);

    DateTimeFormatter myFormatObj = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");

    String formattedDate = myObj.format(myFormatObj);
    System.out.println("After formatting: " + formattedDate);

  }
}