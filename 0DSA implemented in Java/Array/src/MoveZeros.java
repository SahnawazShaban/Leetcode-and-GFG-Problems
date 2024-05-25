import javax.swing.*;

public class MoveZeros {
    static void printArray(int[] arr){
        for (int i=0;i<arr.length;i++) {
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
        int i=0;
        int j=arr.length-1;
        while (i<j){
            swapNumber(arr,i,j);
            i++;
            j--;
        }
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

    static void moveZeroes(int[] nums) {
        if(nums == null || nums.length <=1)
            return;
        int last = -1;
        for(int i=0; i<nums.length; i++){
            if(nums[i] != 0){
                nums[++last] = nums[i];
                if(i != last)
                    nums[i]=0;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {0,1,0,0,2,3,14};
        int i=0,j=arr.length-1;
        printArray(arr);
//        sortZeroOne(arr);
//        reverse(arr);
        moveZeroes(arr);
        printArray(arr);
    }
}
