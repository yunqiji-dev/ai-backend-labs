import java.util.Scanner;

public class SumOfNumbers {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int sum = 0;
        while(true) {
            System.out.println("Give a number:");
            int num = Integer.valueOf(scan.nextLine());

            if (num == 0){
                break;
            }
        }
        sum = sum + sum;
        System.out.println("Sum of the numbers: " + sum);
    }
}
