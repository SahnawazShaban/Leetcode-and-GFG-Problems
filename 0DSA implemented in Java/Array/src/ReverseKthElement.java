import java.util.Scanner;

public class ReverseKthElement {
    static void printArray(int[] arr){
        for (int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
//    static int[] reverseRotate(int[] arr, int k){
//        int n=arr.length;
//        k = k % n;
//        int[] ans = new int[n];
//        int j=0;
//
//        for (int i=n-k;i<n;i++){
//            ans[j++] = arr[i];
//        }
//
//        for (int i=0;i<n-k;i++){
//            ans[j++]=arr[i];
//        }
//        return ans;
//    }

    static void reverseInGroups(int[] arr, int k) {
        // code here
        int start=0,end=k-1;

        while(start<end & k>0){
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;

            start++;
            end--;
        }
    }
    static void swapNumber(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    static void reverse(int[] arr, int i, int j){
//        i=0;
//        j=arr.length-1;
        while (i<j){
            swapNumber(arr,i,j);
            i++;
            j--;
        }
    }

    static void reverseInPlaceRotate(int[] arr,int k){
        int n=arr.length;
        k = k % n;

        reverse(arr,0,n-k-1);
        reverse(arr,n-k,n-1);
        reverse(arr,0,n-1);
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
        System.out.println("Enter Kth value : ");
        int k=sc.nextInt();

        System.out.println("Before Rotation.");
        printArray(arr);
//
//        int[] ans = reverseRotate(arr,k);
//
//        System.out.println("After Rotation.");
//        printArray(ans);

//        reverseInPlaceRotate(arr,k);
//        System.out.println("After Rotation.");
//        printArray(arr);


        reverseInGroups(arr,k);
        System.out.println("After Kth rotation : ");
        printArray(arr);
    }
}
