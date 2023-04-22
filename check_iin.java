import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int m[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 };
        int n[] = {3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2 };
        System.out.println("IIN");
        String text = in.nextLine();
        String[] IIN = text.split("");
        int k[] = new int[IIN.length];
        for (int i = 0; i < IIN.length; i++){
            k[i] = Integer.parseInt(IIN[i]);
        }
        int result = 0;
        for (int i = 0; i < m.length; i++){
            result = result + (k[i] * m[i]);
        }
        int mainResult = result;
        result = 0;
        if (mainResult % 11 == 10){
            for (int i = 0; i < m.length; i++){
                result = result + (k[i] * n[i]);
            }
            System.out.println(result % 11);
        }
        else {
            System.out.println(mainResult % 11);
        }
    }
}
