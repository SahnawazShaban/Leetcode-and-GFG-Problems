import java.util.Scanner;
public class SimpleInterest {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

//        SI = PRT/100
        System.out.println("Enter Principle : ");
        int P = sc.nextInt();

        System.out.println("Enter Rate : ");
        int R = sc.nextInt();

        System.out.println("Enter Time : ");
        int T = sc.nextInt();

        float SI = (P*R*T)/100;

        System.out.println("Simple Interest is : "+SI);

    }
}
