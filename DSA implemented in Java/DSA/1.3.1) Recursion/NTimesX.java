import java.util.Scanner;

public class NTimesX {

    static void nTimes(int x,int n,int ans){
        if (n==0){
            System.out.println(ans);
            return;
        }
        ans = ans*x;

        nTimes(x,n-1,ans);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter value of x : ");
        int x = sc.nextInt();

        System.out.println("Enter value of n : ");
        int n = sc.nextInt();

        nTimes(x,n,1);
    }
}
