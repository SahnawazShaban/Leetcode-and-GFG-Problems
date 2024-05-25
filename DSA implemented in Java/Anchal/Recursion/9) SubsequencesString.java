import java.util.ArrayList;
import java.util.List;

class Solution {
    // Function to generate subsequences
    private List<String> subSequences(int idx, String str, String newstr) {
        List<String> res = new ArrayList<>();
        if (idx >= str.length()) {
            res.add(newstr);
            return res;
        }

        newstr += str.charAt(idx);
        res.addAll(subSequences(idx + 1, str, newstr));

        // Exclude the current character from the subsequence
        newstr = newstr.substring(0, newstr.length() - 1);

        res.addAll(subSequences(idx + 1, str, newstr));

        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String str = "abc";
        List<String> res = solution.subSequences(0, str, "");
        System.out.println(res);
    }
}
