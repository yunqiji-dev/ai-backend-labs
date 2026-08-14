
import java.util.Scanner;

public class Story {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);

        // Write your program here
        System.out.println("I will tell you a story, but I need some information first.\n" + //
                        "What is the main character called?");

        String name = reader.nextLine();

        System.out.println("What is their job?");

        String job = reader.nextLine();

        System.out.println("Here is the story:\n" + //
                        "Once upon a time there was " + name + ", who was a " + job + ".\n" + //
                        "On the way to work, " + name + " reflected on life.\n" + //
                        "Perhaps " + name + " will not be a " + job + " forever.");

    }
}
