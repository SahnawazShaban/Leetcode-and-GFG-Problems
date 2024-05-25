import java.util.Scanner;
public class Main {
    int sum(int a, int b){
        return a+b;
    }
    public static void main(String[] args) {
        Main sh=new Main();
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter value of x : ");
        int x=sc.nextInt();
        System.out.println("Enter value of y : ");
        int y=sc.nextInt();
        System.out.print("Sum is ");
        System.out.println(sh.sum(x,y));
    }
}