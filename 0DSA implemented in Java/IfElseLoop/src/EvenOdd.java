import java.util.Scanner;
public class EvenOdd {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter number : ");
        int age=sc.nextInt();

//        if(num%2==0){
//            System.out.println(num + " is even number.");
//        }
//        else {
//            System.out.println(num + " is odd number.");
//        }

        if(age<12){
            System.out.println("Child");
        }
        else if (age<=18 && age>=12) {
            System.out.println("Teenager");
        }
        else {
            System.out.println("Adult");
        }
    }
}
