import java.util.Scanner;
public class Pattern3 {
    public static void main(String[] args) {
//        for (int i=5;i>0;i--){
//            for (int j=0;j<i;j++){
//                System.out.print("*");
//            }
//            System.out.println("");
//        }
//
//        *****
//        ****
//        ***
//        **
//        *

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter value of n : ");
        int n = sc.nextInt();

        for (int i=1;i<=n;i++){
            for (int j=1;j<=(n+1-i);j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
