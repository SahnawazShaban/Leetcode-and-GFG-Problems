import java.util.Stack;

public class PrefixExpression {
    public static void main(String[] args) {
        // HOMEWORK
        // ans,infix,prefix
//        String exp = "-+2/*6483";

        int[] nums = {4,2,3};

        int min = nums[0];

        for (int i=0;i< nums.length;i++){
            min = Math.min(min,nums[i]);
        }
//        System.out.println(min);

        int sum = 0;

        for (int i=0;i<nums.length;i++){
            sum += nums[i];
        }
//        System.out.println(sum);

        System.out.println(sum-min);
    }
}
