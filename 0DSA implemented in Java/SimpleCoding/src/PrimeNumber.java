import java.util.Scanner;

public class PrimeNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number :");
        int n = sc.nextInt();
//        int flag = 0;

        if (n == 0 || n == 1){
            System.out.println(n+ " is not a prime number.");
        }

        long count = 0;

        for (int j=2;j<=n;j++) {
            int flag = 0;
            for (int i = 2; i < j; i++) {
                if (j % i == 0) {
//                    System.out.println(j + " is not prime");
                    flag = 1;
                    break;
                }
            }
            if (flag == 0) {
                count++;
//                System.out.println(j+" is prime");
            }
        }

        System.out.println(count);
    }
}
