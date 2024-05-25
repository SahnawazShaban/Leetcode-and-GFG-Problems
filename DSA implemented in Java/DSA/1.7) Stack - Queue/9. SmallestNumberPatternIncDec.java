import java.util.Stack;

public class SmallestNumberPatternIncDec {
    public static void main(String[] args) {
        String pat = "ddidddid";

        Stack<Integer> st = new Stack<>();
        int num = 1;

        for (int i=0;i<pat.length();i++){
            char ch = pat.charAt(i);

            if (ch == 'd'){
                st.push(num);
                num++;
            }
            else {
                st.push(num);
                num++;

                while (st.size() > 0){
                    System.out.println(st.pop());
                }
            }
        }
        st.push(num);

        while (st.size() > 0){
            System.out.println(st.pop());
        }
    }
}
