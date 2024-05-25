import java.util.Stack;

public class PushPopPeek {
    public static void main(String[] args) {
        Stack<Integer> st = new Stack<>();

        st.push(12);
        st.push(20);
        st.push(40);
        st.push(10);
        st.push(50);

        st.pop();  // pop : 50

        System.out.println(st);

        System.out.println("Peek Elements : " + st.peek() + "\nSize : " + st.size());

        //If stack size is empty then peek goes to runtime error
    }
}
