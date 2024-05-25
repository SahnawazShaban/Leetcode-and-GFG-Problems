import java.util.Scanner;
import java.util.Stack;

public class InfixOperation {
    public static int precedence(char op){
        if(op == '+'){
            return 1;
        } else if (op == '-') {
            return 1;
        } else if (op == '*') {
            return 2;
        }
        else {
            return 2;
        }
    }

    public static int operation(int v1, int v2, char op){
        if(op == '+'){
            return v1+v2;
        } else if (op == '-') {
            return v1-v2;
        } else if (op == '*') {
            return v1*v2;
        }
        else {
            return v1/v2;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String exp = sc.nextLine();

        Stack<Integer> operand = new Stack<>();
        Stack<Character> operator = new Stack<>();

        for (int i=0;i<exp.length();i++){
            char ch = exp.charAt(i);

            if (ch == '('){
                operator.push(ch);
            }
            else if (Character.isDigit(ch)){
                operand.push(ch - '0');
            }
            else if (ch == ')') {
                while (operator.peek() != '(') {
                    char opr = operator.pop();

                    int v2 = operand.pop();
                    int v1 = operand.pop();

                    int op = operation(v1,v2,opr);
                    operand.push(op);
                }
                operator.pop();
            }
            else if (ch == '+' || ch == '-' || ch == '*' || ch == '/'){
                while (operator.size() > 0 && operator.peek() != '(' && precedence(ch) <= precedence(operator.peek())){
                    char opr = operator.pop();

                    int v2 = operand.pop();
                    int v1 = operand.pop();

                    int op = operation(v1,v2,opr);
                    operand.push(op);
                }
                operator.push(ch); // after completion of loop those operator is added into operator stack.
            }
        }

        while (operator.size() != 0){
            char opr = operator.pop();

            int v2 = operand.pop();
            int v1 = operand.pop();

            int op = operation(v1,v2,opr);
            operand.push(op);
        }
        System.out.println(operand.peek());
    }
}
