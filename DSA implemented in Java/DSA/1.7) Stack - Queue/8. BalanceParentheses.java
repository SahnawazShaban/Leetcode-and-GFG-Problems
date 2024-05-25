import java.util.Scanner;
import java.util.Stack;

public class BalanceParentheses {
    public static boolean handleClosing(Stack<Character> st, char peekEle){
        if(st.size() == 0){
            return false;
        }
        else if (st.peek() != peekEle) {
            return false;
        }
        else {
            st.pop();
            return true;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Stack<Character> st = new Stack<>();
        System.out.println("Enter String : ");
        String str = sc.nextLine();

        for (int i=0;i<str.length();i++){
            char ch = str.charAt(i);

            if (ch == '(' || ch == '{' || ch == '['){
                st.push(ch);
            }
            else if (ch == ')') {
                boolean val = handleClosing(st,'(');
                if(val == false){
                    System.out.println(val);
                    return;
                }
            }
            else if (ch == '}') {
                boolean val = handleClosing(st,'{');
                if(val == false){
                    System.out.println(val);
                    return;
                }
            }
            else if (ch == ']') {
                boolean val = handleClosing(st,'[');
                if(val == false){
                    System.out.println(val);
                    return;
                }
            }
            else {

            }
        }
        if (st.size() == 0){
            System.out.println(true);
        }
        else {
            System.out.println(false);
        }
    }
}
