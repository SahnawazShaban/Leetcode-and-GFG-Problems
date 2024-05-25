public class RemoveDuplicateElementInPlace {
    public static void main(String[] args) {
        int[] nums = {1,91,2,3,3,3,1,4,2,1,10};
        System.out.println(nums[Math.abs(1)]);
        int i=0;
        for (int val : nums){
            if(i<1 || val > nums[i-1]){
                nums[i] = val;
                i++;
            }
        }

        System.out.println("No. of unique elements : " + i);
    }
}
