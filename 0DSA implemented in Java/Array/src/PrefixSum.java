import java.util.Scanner;

public class PrefixSum {
    static void printArray(int[] arr){
        for (int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
    static void prefixSum(int[] arr){
        int n = arr.length;
//        int[] pref = new int[n];
//
//        pref[0] = arr[0];  - > with extra space
        for (int i=1;i<n;i++){
            arr[i] = arr[i] + arr[i-1]; // without extra space
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter value of n : ");
        int n = sc.nextInt();
        int[] arr = new int[n];

        System.out.println("Enter "+n+" elements.");

        for (int i=0;i<arr.length;i++){
            arr[i] = sc.nextInt();
        }

        prefixSum(arr);
        printArray(arr);
    }
}
