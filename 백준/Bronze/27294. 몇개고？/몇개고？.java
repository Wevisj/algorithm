import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int time = scanner.nextInt();
        int drink = scanner.nextInt();

        if (12 <= time && time <= 16 && drink == 0)
            System.out.println(320);

        else
            System.out.println(280);
    }
}
