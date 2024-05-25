import java.util.Scanner;

public class SortArray {
    static void printArray(int[] arr){
        for (int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
    static void swapNumber(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    static void sortZeroOne(int[] arr){
        int n=arr.length;
        int count=0;

        // Count number of Zeroes
        for (int i=0;i<n;i++){
            if (arr[i] == 0){
                count++;
            }
        }
        //0 to count-1 : 0, count to n-1 : 1
        for (int i=0;i<n;i++){
            if (i<count){
                arr[i]=0;
            }
            else {
                arr[i]=1;
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter n value : ");
        int n = sc.nextInt();

        int[] arr=new int[n];

        System.out.println("Enter Elements : ");
        for (int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }

        System.out.println("Before Sort : ");
        printArray(arr);

        sortZeroOne(arr);
        System.out.println("After Sort : ");
        printArray(arr);
    }
}
