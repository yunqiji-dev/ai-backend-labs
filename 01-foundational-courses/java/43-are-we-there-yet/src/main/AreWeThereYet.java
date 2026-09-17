import java.util.Scanner;

public class AreWeThereYet {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        while(true) {
            System.out.println("Give a number:");
            int num = Integer.valueOf(scan.nextLine());

            if (num == 4){
                break;
            }
        }
    }
}