import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int n = sc.nextInt();

        for (int i = 0; i < n; ++i) {
            sb.append(" ".repeat(Math.max(0, n - 1 - i)));
            sb.append("*".repeat(i + 1));
            sb.append("\n");
        }
        System.out.println(sb);
    }

}
