import java.util.ArrayList;
import java.util.List;

class Solution {
    // Function to generate power set
    private void powerSet(int idx, int[] arr, List<Integer> arr1, List<List<Integer>> res) {
        // If the index is equal to or exceeds the length of the array,
        // add the current subset to the result if it's not already present.
        if (idx >= arr.length) {
            if (!res.contains(arr1)) {
                res.add(new ArrayList<>(arr1));
            }
            return;
        }

        // Include the current element in the subset and recursively generate subsets.
        arr1.add(arr[idx]);
        powerSet(idx + 1, arr, arr1, res);

        // Exclude the current element from the subset and recursively generate subsets.
        arr1.remove(arr1.size() - 1);
        powerSet(idx + 1, arr, arr1, res);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] arr = {2, 1, 3};
        List<List<Integer>> res = new ArrayList<>(); // List to store the power set
        solution.powerSet(0, arr, new ArrayList<>(), res); // Start generating power set from index 0
        System.out.println(res);
    }
}
