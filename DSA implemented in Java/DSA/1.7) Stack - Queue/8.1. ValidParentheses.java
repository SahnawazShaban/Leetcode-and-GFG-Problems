import java.util.Scanner;
import java.util.Stack;

public class ValidParentheses {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        Stack<Character> st = new Stack<>();

        for(int i=0;i<s.length();i++){
            char ch = s.charAt(i);
            if(ch == '(' || ch == '{' || ch == '['){
                st.push(ch);
            }
            else if(ch == ')' && st.pop() != '('){
                System.out.println("false");
                return;
            }
            else if(ch == '}' && st.pop() != '{'){
                System.out.println("false");
                return;
            }
            else if(ch == ']' && st.pop() != '['){
                System.out.println("false");
                return;
            }
        }
        if(st.empty()){
            System.out.println("true");
            return;
        }
        else {
            System.out.println("false");
        }
    }
}
