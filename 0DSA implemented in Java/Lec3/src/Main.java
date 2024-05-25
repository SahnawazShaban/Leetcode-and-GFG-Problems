import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
//        int age = 22;
//        String name = "Shaan";
//
//        System.out.println("Value is "+ age);
//        System.out.println("Name is "+ name);


//        INPUT

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your name : ");
        String name = sc.next();
        System.out.println("Your name is "+name);

        System.out.println("Enter your age : ");
        int age = sc.nextInt();
        System.out.println("Your age is "+age);
    }
}