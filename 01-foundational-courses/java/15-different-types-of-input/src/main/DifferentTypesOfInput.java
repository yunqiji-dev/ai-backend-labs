
import java.util.Scanner;

public class DifferentTypesOfInput {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Write your program here
        System.out.println("Give a string: ");
        String text = scanner.nextLine();
        System.out.println("You give the string " + text);

        System.out.println("Give a integer: ");
        int integer = Integer.valueOf(scanner.nextLine());
        System.out.println("You give the integer " + integer);

        System.out.println("Give a double: ");
        double floatingPoint = Double.valueOf(scanner.nextLine());
        System.out.println("You give the double " + floatingPoint);

        System.out.println("Give me a boolean: ");
        boolean trueOrFalse = Boolean.valueOf(scanner.nextLine());
        System.out.println("You give the boolean " + trueOrFalse);


    }
}
