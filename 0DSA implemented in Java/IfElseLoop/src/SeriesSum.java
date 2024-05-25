import java.util.Scanner;
public class SeriesSum {
    public static void main(String[] args) {
//        SERIES = 1 - 2 + 3 - 4 ..... n
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Last Number : ");

        int last = sc.nextInt();
        int num = 1;
        int sum = 0;

        while (last >= num){
            if (num%2==0){
                sum = sum - num;
                num++;
            }
            else {
                sum = sum + num;
                num++;
            }
        }
        System.out.println("Series Sum is "+sum);
    }
}
