import java.util.Scanner;
public class ARaiseB {
    public static void main(String[] args) {
        
//        3^2 = 9 (3 times 2)

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter value of A : ");
        int a = sc.nextInt();

        System.out.println("Enter value of B : ");
        int b = sc.nextInt();
        int ans = 1;

        for (int i=1;i<=b;i++){
            ans = ans*a;
        }
        System.out.println(ans);
    }
}
