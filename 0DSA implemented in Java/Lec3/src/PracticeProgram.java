import java.util.Scanner;

public class PracticeProgram {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int fact = 1;
        int num1 = num;

        while (num!=0){
            fact = fact*num;
            num--;
        }
        System.out.println("Factorial of "+ num1 +" is "+fact);
    }
}
