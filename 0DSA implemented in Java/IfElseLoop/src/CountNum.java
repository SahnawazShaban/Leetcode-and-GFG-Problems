import java.util.Scanner;
public class CountNum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number : ");
        int num = sc.nextInt();

//        Count number

//        int count = 0;
//
//        while (num!=0){
//            count++;
//            num/=10;
//        }
//        System.out.println(count);

//        Sum of each digit

//        int sum = 0;
//
//        while (num!=0){
//            int rem = num%10;
//            sum+=rem;
//            num/=10;
//        }
//        System.out.println(sum);

//        Reverse number

        int ans = 0;

        while (num!=0){
            int rem = num%10;
            ans = ans*10 +rem;
            num/=10;
        }
        System.out.println(ans);
    }
}
