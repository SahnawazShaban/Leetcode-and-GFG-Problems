import java.util.Scanner;
import java.lang.Math;

public class DecimalToBinary {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter value of n : ");
        int n=sc.nextInt();
        int ans=0,i=0;

        while (n!=0){
            int bit = n&1;
            ans = (int) (bit * Math.pow(10,i) + ans);
            n = n>>1;
            i++;
        }
        System.out.println("Decimal 2 Binary : "+ans);
    }
}
