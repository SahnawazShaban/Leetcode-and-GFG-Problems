import java.util.ArrayList;
import java.util.List;

class Solution {
    // Function to generate subsequences
    private List<List<Integer>> subSequences(int idx, int[] arr, List<Integer> arr1) {
        List<List<Integer>> res = new ArrayList<>();
        if (idx >= arr.length) {
            res.add(new ArrayList<>(arr1));
            return res;
        }

        arr1.add(arr[idx]);
        res.addAll(subSequences(idx + 1, arr, arr1));

        arr1.remove(arr1.size() - 1);
        res.addAll(subSequences(idx + 1, arr, arr1));

        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] arr = {3, 1, 2};
        List<List<Integer>> res = solution.subSequences(0, arr, new ArrayList<>());
        System.out.println(res);
    }
}
