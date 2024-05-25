import java.util.Stack;

public class ReverseStringUsingStack {
    public static void main(String[] args) {
        String s = "leetcode";

        Stack<Character> st = new Stack<>();
        int len = s.length()-1;
        for (int i =len;i>=0;i--){
            char ch = s.charAt(i);
            //just print elements
            System.out.print(ch);

            //if elements store into stack
            st.push(ch);
        }
        System.out.println(); // next line
        System.out.println(st);

        // for traverse a stack elements or values
        while (!st.isEmpty()){
            char ch = st.pop();
            System.out.print(ch + " ");
        }
    }
}
