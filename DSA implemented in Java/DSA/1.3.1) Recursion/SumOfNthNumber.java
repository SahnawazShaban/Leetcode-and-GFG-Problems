import java.util.Scanner;

public class SumOfNthNumber {
    public static void printSum(int i,int n,int sum){
        if (i > n){
            System.out.println(sum);
            return;
        }
        sum += i;
        printSum(i+1,n,sum);
        System.out.println(sum);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter N value : ");
        int n = sc.nextInt();

        printSum(1,n,0);
    }
}
