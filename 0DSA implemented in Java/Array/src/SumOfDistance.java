import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SumOfDistance {
    public static void main(String[] args) {
//        Input: nums = [1,3,1,1,2]
//        Output: [5,0,3,4,0]
//        Explanation:
//        When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5.
//        When i = 1, arr[1] = 0 because there is no other index with value 3.
//        When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3.
//        When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4.
//        When i = 4, arr[4] = 0 because there is no other index with value 2.

//        int[] nums = {1,5,1,1,2};
//        int[] arr = new int[nums.length];
//        int k=0;
//
//        for (int i=0;i<nums.length;i++){
//            int val = 0;
//            for (int j=0;j<nums.length;j++){
//                if (nums[i] == nums[j]){
//                    val = val + Math.abs(i-j);
//                }
//            }
//            arr[k] = val;
//            k++;
//        }
//
//        for (int value : arr){
//            System.out.print(value+" ");
//        }

        int[] arr = {1,5,1,1,2};

        Map<Integer, List<Integer>> m = new HashMap<>();
        long[] res = new long[arr.length];
        for (int i = 0; i < arr.length; i++) {
            if (!m.containsKey(arr[i])) m.put(arr[i], new ArrayList<>());
            m.get(arr[i]).add(i);
        }
        for (int x: m.keySet()) {
            List<Integer> l = m.get(x);
            long[] pre = new long[l.size() + 1];
            for (int i = 0; i < l.size(); i++)
                pre[i + 1] = pre[i] + (int)l.get(i);
            for (int i = 0; i < l.size(); i++) {
                long v = (long)(int)l.get(i);
                res[(int)l.get(i)] = (v * (i + 1) - pre[i + 1])
                        + ((pre[l.size()] - pre[i]) - v * (l.size() - (i)));
            }
        }

        for (long val : res){
            System.out.print(val+" ");
        }
    }
}
