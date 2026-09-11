import java.util.Scanner;

public class Squared {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int num = Integer.valueOf(scan.nextLine());
        int square = num * num;
        System.out.println(square);
}
}
