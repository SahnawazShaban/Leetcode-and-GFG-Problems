import java.util.Scanner;

public class SortArray01 {
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
        int left = 0;
        int right = arr.length-1;

        while (left<right){
            if (arr[left] == 1 & arr[right]==0){
                swapNumber(arr,left,right);
                left++;
                right--;
            }
            else if (arr[left]==0){
                left++;
            }
            else {
                right--;
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
