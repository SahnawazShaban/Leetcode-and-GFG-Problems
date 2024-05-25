import java.util.Scanner;

public class SwapNumber {
    static void printArray(int[] arr){
        for (int i=0;i<arr.length;i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
    static void swapNumber(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    static void reverse(int[] arr){
        int start=0,end=arr.length-1;
        while (start<end){
            swapNumber(arr,start,end);
            start++;
            end--;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter n value : ");
        int n=sc.nextInt();
        int[] arr=new int[n];

        System.out.println("Enter your element : ");
        for (int i=0;i<arr.length;i++){
            arr[i] = sc.nextInt();
//            System.out.println(arr[i]);
        }
//        original array-
//        printArray(arr);
//        System.out.println("Enter first number : ");
//        int a=sc.nextInt();
//        System.out.println("Enter second number : ");
//        int b=sc.nextInt();

//        with extra variable
//        int temp = a;
//        a=b;
//        b=temp;

//        without extra variable
//        a=a+b;
//        b=a-b;
//        a=a-b;

        reverse(arr);
        printArray(arr);
    }
}
