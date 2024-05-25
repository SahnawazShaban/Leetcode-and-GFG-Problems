import java.util.Scanner;

public class SqrtNonDecreasing {
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
    static void reverse(int[] arr){
        int i=0, j=arr.length-1;
        while (i<j){
            swapNumber(arr,i,j);
            i++;
            j--;
        }
    }

    static int[] sqrtOfElement(int[] arr){
        int n=arr.length;
        int i=0,j=n-1;
        int[] ans=new int[n];
        int k=n-1;
        while (i<=j){
            if (Math.abs(arr[i]) > Math.abs(arr[j])){
                ans[k--]=arr[i]*arr[i];
                i++;
            }
            else {
                ans[k--]=arr[j]*arr[j];
                j--;
            }
        }
        return ans;
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

        System.out.println("Before Sqrt : ");

        printArray(arr);

        int[] ans = sqrtOfElement(arr);
        System.out.println("After Sqrt : ");

//        reverse(ans);
        printArray(ans);
    }
}
