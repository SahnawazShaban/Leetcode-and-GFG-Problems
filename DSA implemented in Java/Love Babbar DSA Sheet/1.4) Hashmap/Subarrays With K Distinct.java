/*
Subarrays With K Distinct

*/

// SOLUTION
import java.util.*;

class SubarraysWithKDistinct {
    static int subarraysWithKDistinctBetter(int[] nums, int k) {
        int count = 0;
        int windowStart = 0;
        HashMap<Integer, Integer> charFreq = new HashMap<>();
        for (int windowEnd = 0; windowEnd < nums.length; windowEnd++) {
            charFreq.put(nums[windowEnd], charFreq.getOrDefault(nums[windowEnd], 0) + 1);
            while (charFreq.size() > k) {
                charFreq.put(nums[windowStart], charFreq.get(nums[windowStart]) - 1);
                if (charFreq.get(nums[windowStart]) == 0) {
                    charFreq.remove(nums[windowStart]);
                }
                windowStart++;
            }
            if (charFreq.size() == k) {
                count += windowEnd - windowStart + 1;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int[] nums = {1,2,1,3,4};

        int ans = subarraysWithKDistinctBetter(nums, 3);

        System.out.println(ans);
    }

}
