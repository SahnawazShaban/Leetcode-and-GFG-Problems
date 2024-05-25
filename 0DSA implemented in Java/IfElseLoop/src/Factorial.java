import java.util.Scanner;
public class Factorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Number :");
        int num = sc.nextInt();
        int fact = 1;

//        while (num != 0){
//            fact *= num;
//            num--;
//        }
//        System.out.println(fact);

//        LIST OF FACTORIAL
        for (int i=1;i<=num;i++){
            fact = fact*i;

            System.out.println(i+" : "+fact);
        }
    }
}
