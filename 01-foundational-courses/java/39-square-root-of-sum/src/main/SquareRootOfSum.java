import java.util.Scanner;

public class SquareRootOfSum {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int num1 = Integer.valueOf(scan.nextLine());
        int num2 = Integer.valueOf(scan.nextLine());

        int sum = num1 + num2;
        double result = Math.sqrt(sum);
        System.out.println(result);
    }
}
