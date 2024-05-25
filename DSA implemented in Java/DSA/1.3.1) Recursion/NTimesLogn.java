import java.util.Scanner;

public class NTimesLogn {
    static int nTimesLogn(int x,int n){
        if (n==0){
            return 1;
        }

        if (x==0){
            return 0;
        }

        if (n%2 == 0){
            return nTimesLogn(x,n/2) * nTimesLogn(x,n/2);
        }
        else {
            return nTimesLogn(x,n/2) * nTimesLogn(x,n/2) * x;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter value of x : ");
        int x = sc.nextInt();

        System.out.println("Enter value of n : ");
        int n = sc.nextInt();

        int ans=nTimesLogn(x,n);

        System.out.println(ans);
    }
}
