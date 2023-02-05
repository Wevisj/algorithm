import java.util.Scanner;

public class Main {
    public static boolean[][] arr;
    public static int min = 64;

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int M = scanner.nextInt();

        arr = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            String str = scanner.next();
            for (int j = 0; j < M; j++) {
                arr[i][j] = str.charAt(j) == 'W';
            }
        }

        int row = N - 7;
        int col = M - 7;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                find(i, j);
            }
        }

        System.out.println(min);
    }

    public static void find(int x, int y) {
        int end_x = x + 8;
        int end_y = y + 8;
        int count = 0;

        boolean check_color = arr[x][y];

        for (int i = x; i < end_x; i++) {
            for (int j = y; j < end_y; j++) {
                if (arr[i][j] != check_color)
                    count++;
                check_color = (!check_color);
            }
            check_color = !check_color;
        }

        count = Math.min(count, 64 - count);

        min = Math.min(min, count);
    }
}