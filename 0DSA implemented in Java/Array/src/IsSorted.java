import java.util.Arrays;

public class IsSorted {
//    static int[] smallestElementAndLargestElement(int arr){
//        Arrays.sort(arr);
//        int[] ans = {arr[0], arr[arr.length-1]};
//        return ans;
//    }
    static  boolean isSorted(int[] arr){
        boolean check = true;
        for (int i=1;i<arr.length;i++){
            if (arr[i]<arr[i-1]){
                check = false;
                break;
            }
        }
        return check;
    }
    public static void main(String[] args) {
        int[] arr = {2,4,5,6,6,8,9,9,88,9};
        boolean ans = isSorted(arr);

        if (ans == true){
            System.out.println("Sorted");
        }
        else {
            System.out.println("Not Sorted");
        }

//        smallestElementAndLargestElement(arr)

    }
}
