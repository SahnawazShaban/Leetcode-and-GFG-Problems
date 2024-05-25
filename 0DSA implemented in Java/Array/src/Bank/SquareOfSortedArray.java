package Bank;

public class SquareOfSortedArray {
    static void printArray(int[] nums){
        for (int i=0;i<nums.length;i++){
            System.out.print(nums[i] + " ");
        }
        System.out.println();
    }
    static int[] sortedSquares(int[] nums) {
        int j=0;
        for(int i=0;i<nums.length;i++){
            nums[j++] = nums[i]*nums[i];
        }

        for(int p=0;p<nums.length;p++){
            for(int q=p+1;q<nums.length;q++){
                if(nums[p]>nums[q]){
                    int temp = nums[p];
                    nums[p] = nums[q];
                    nums[q] = temp;
                }
            }
        }
        return nums;
    }
    public static void main(String[] args) {
        int[] nums = {-4,-1,0,3,10,12,8};
        printArray(nums);
        int[] ans = sortedSquares(nums);
        printArray(nums);
    }
}
