import java.util.Stack;

public class PrefixPostfixEvaluation {
    public static int precedence(char ch){
        if (ch == '+' || ch == '-'){
            return 1;
        } else if (ch == '*' || ch == '/') {
            return 2;
        }
        else {
            return 0;
        }
    }

    public static void evaluation(Stack<String> postfix,Stack<String> prefix, Stack<Character> operator){
        char op = operator.pop();

        String prev2 = prefix.pop();
        String prev1 = prefix.pop();
        String preopr = op + prev1 + prev2;
        prefix.push(preopr);

        String postv2 = postfix.pop();
        String postv1 = postfix.pop();
        String postop = postv1 + postv2 + op;
        postfix.push(postop);
    }

    public static void main(String[] args) {
        Stack<String> postfix = new Stack<>();
        Stack<String> prefix = new Stack<>();

        Stack<Character> operator = new Stack<>();

        String exp = "a+(b*c)";

        for (int i=0;i<exp.length();i++){
            char ch = exp.charAt(i);

            if (ch == '('){
                operator.push(ch);
            }
            else  if ((ch  >= '0' && ch <= '9' ) || (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
                prefix.push(ch + "");
                postfix.push(ch + "");
            }
            else if (ch == ')') {
                while (operator.peek() != '('){
                    evaluation(postfix,prefix,operator);
                }
                operator.pop();
            }
            else if (ch == '+' || ch == '-' || ch == '*' || ch == '/') {
                while (operator.size() > 0 && operator.peek() != '(' && precedence(ch) <= precedence(operator.peek())) {
                    evaluation(postfix,prefix,operator);
                }
                operator.push(ch); // pushing current operator
            }
        }

        while (operator.size() > 0){
            evaluation(postfix,prefix,operator);
        }

        System.out.println("Postfix : " + postfix.peek());
        System.out.println("Prefix : " + prefix.peek());
    }
}
