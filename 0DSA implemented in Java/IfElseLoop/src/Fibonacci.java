import java.util.Scanner;
public class Fibonacci {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("How many number you get of Fibonacci : ");
        int num = sc.nextInt();

        int first = 0, second=1, next=0;
        System.out.print(first+" , "+second+" , ");

        while (num-2!=0){
            next = first+second;
            System.out.print(next+" , ");
            first=second;
            second=next;
            num--;
        }
    }
}
