import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Filehandling {
    public static void main(String[] args) {
        try {
            File myfile = new File("filename.txt");
            if(myfile.createNewFile()) {
                System.out.println("File created: " + myfile.getName());
            }
            else {
                System.out.println("File already exists.");
            }
        }catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    

    try {
        FileWriter mywriter = new FileWriter("filename.txt");
        mywriter.write("The file is written - this is how to write a file in java");
        mywriter.close();
        System.out.println("Successfully writtern");
    } catch(IOException e) {
        System.out.println("An error occurred.");
        e.printStackTrace();
    }

try {
    File myfile = new File("filename.txt");
    Scanner myreader = new Scanner(myfile);
    while(myreader.hasNextLine()) {
        String data = myreader.nextLine();
        System.out.println(data);
    }
    myreader.close();

} 
   catch(FileNotFoundException e) {
    System.out.println("An error occurred.");
    e.printStackTrace();
}

File myfile = new File("filename.txt");
if(myfile.exists()) {
    System.out.println("File name: " + myfile.getName());
      System.out.println("Absolute path: " + myfile.getAbsolutePath());
      System.out.println("Writeable: " + myfile.canWrite());
      System.out.println("Readable " + myfile.canRead());
      System.out.println("File size in bytes " + myfile.length());
} 
else {
    System.out.println("The file does not exist.");
}


    if (myfile.delete()) { 
      System.out.println("Deleted the file: " + myfile.getName());
    } else {
      System.out.println("Failed to delete the file.");
    } 
    }
} 


