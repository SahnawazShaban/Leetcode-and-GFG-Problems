import java.util.Scanner;

public class PrintNNaturalNumber {
    static void nNaturalNumber(int num){
//        System.out.println(" "+num);
        if (num>1){
            nNaturalNumber(num-1);
        }
        System.out.println(" "+num);

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Nth number : ");
        int num = sc.nextInt();
        nNaturalNumber(num);
    }
}
