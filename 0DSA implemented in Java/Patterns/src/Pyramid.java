import java.util.Scanner;
public class Pyramid {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter value of n : ");

        int n = sc.nextInt();

        for (int i=1;i<=n;i++){
//            this loop for space (r-i)
            for (int j=1;j<=n-i;j++){
                System.out.print(" ");
            }

//            this loop for star (2*i-1)
            for (int k=1;k<=(2*i-1);k++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
