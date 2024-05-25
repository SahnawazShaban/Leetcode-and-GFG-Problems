public class MaxSumSubarray {
    public static int longestSubarray(int[] A) {
        int i = 0, j, k = 1;
        for (j = 0; j < A.length; j++) {
            if (A[j] == 0)
                k--;
            if (k < 0 && A[i++] == 0)
                k++;
        }
        return j - i;
    }
    public static void main(String[] args) {
        int[] A = {1,0,1,1,0,0,0,1,1,0,1,1};
        int ans = longestSubarray(A);
        System.out.println(ans);
    }
}
