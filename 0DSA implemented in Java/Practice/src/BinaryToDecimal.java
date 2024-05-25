import java.util.Scanner;
import java.lang.Math;

public class BinaryToDecimal {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
//        11101
        System.out.println("Enter a value in form of binary : ");
        int n=sc.nextInt();

        int ans=0,i=0;

        while (n!=0){
            int bit = n&1;  // n%10    both are correct.  & - bitwise AND
            ans = (int)(bit * Math.pow(2,i)+ans);
            n = n/10;
            i++;
        }
        System.out.println("Binary to Decimal : "+ans);
    }
}
