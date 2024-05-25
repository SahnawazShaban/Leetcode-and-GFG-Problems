public class JustCheck {
    static void printArray(int[] nums){
        for (int i=0;i<nums.length;i++){
            System.out.print(nums[i]+" ");
        }
        System.out.println();
    }
    static int[] applyOperations(int[] nums) {
        int j=0;
        int n=nums.length;

        for(int i=0;i<n-1;i++){
            if(nums[i] == nums[i+1]){
                nums[i] = nums[i] + nums[i+1];
                nums[i+1] = 0;
            }

            if(nums[i] != 0){
                nums[j++] = nums[i];
            }
        }
        if(nums[n-1] != 0){
            nums[j++] = nums[n-1];
        }

        for(int k=j;k<n;k++){
            nums[k] = 0;
        }

        return nums;
    }
    public static void main(String[] args) {
//        System.out.println("apple".compareTo("Apple"));
        int[] nums = {1,2,2,1,1,0,1};
        printArray(nums);
        int[] ans = applyOperations(nums);
        printArray(ans);
    }
}
