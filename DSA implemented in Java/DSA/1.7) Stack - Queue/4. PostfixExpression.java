import java.util.Stack;

public class PostfixExpression {
    public static int operation(int val1, int val2, char ch){
        if (ch == '+'){
            return val1+val2;
        } else if (ch == '-') {
            return val1-val2;
        } else if (ch == '*') {
            return val1*val2;
        }
        else {
            return val1/val2;
        }
    }
    public static void main(String[] args) {
        String exp = "264*8/+3-";

        Stack<Integer> value = new Stack<>();
        Stack<String> infix = new Stack<>();
        Stack<String> prefix = new Stack<>();

        for (int i=0;i<exp.length();i++){
            char ch = exp.charAt(i);

            if (ch == '+' || ch == '-' || ch == '*' || ch == '/'){
                int val2 = value.pop();
                int val1 = value.pop();
                int val = operation(val1,val2,ch);
                value.push(val);

                String in2 = infix.pop();
                String in1 = infix.pop();
                String stri = "(" + in1 + ch + in2 + ")";
                infix.push(stri);

                String po2 = prefix.pop();
                String po1 = prefix.pop();
                String strp = ch + po1 + po2;
                prefix.push(strp);
            }
            else {
                // for operand
                value.push(ch - '0');
                infix.push(ch + "");
                prefix.push(ch + "");
            }
        }

        System.out.println("Value : "+ value.peek());
        System.out.println("Postfix : "+ exp);
        System.out.println("Infix : "+ infix.peek());
        System.out.println("Prefix : "+ prefix.peek());
    }
}
