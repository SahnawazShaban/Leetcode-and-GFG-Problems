import java.util.Scanner;

public class Factorial {
    static void factorial(int n,int fact,int temp){
        if (n == 0){
            System.out.println("Factorial of "+temp+" is "+fact);
            return;
        }
        fact *= n;
        factorial(n-1,fact,temp);

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Found your factorial : ");

        int n = sc.nextInt();

        factorial(n,1, n);
    }
}
