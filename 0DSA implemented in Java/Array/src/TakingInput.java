import java.util.Scanner;
public class TakingInput {

    static void printArray(int[] arr){
        for (int i=0;i<arr.length;i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
//        System.out.print("How many number do you enter : ");
//        int n=sc.nextInt();
        int[] arr=new int[5];
        System.out.println("Enter your element : ");
        for (int i=0;i<arr.length;i++){
            arr[i] = sc.nextInt();
//            System.out.println("Your "+ (i+1) + " element is "+num);
        }
//        original array-
        printArray(arr);

        int[] arr2 = arr;

//        copied array
        printArray(arr2);
    }
}
