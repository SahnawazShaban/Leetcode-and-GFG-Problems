import java.util.Scanner;
import java.util.Stack;

public class LongestValidParentheses {
    public static int longestValidParentheses(String s) {
        Stack<Character> st = new Stack<>();
        Stack<Integer> idx = new Stack<>();
        idx.push(-1);
        int max = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (ch == '(') {
                st.push(ch);
                idx.push(i);
            } else {
                if (!st.empty() && st.peek() == '(') { //if opening bracket is not there
                    st.pop();
                    idx.pop();
                    max = Math.max(max, i - idx.peek());
                } else {
                    idx.push(i);
                }
            }
        }
        return max;
    }

    public static void main(String[] args) {

//        Scanner sc = new Scanner(System.in);
//        System.out.println("Enter Parentheses : ");
        String str = ")()((())(()()())";

        int ans = longestValidParentheses(str);

        System.out.println("Ans : " + ans);
    }
}
