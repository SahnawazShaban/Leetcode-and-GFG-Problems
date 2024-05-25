import java.util.Stack;

public class NextGreaterElements {
    public static void main(String[] args) {
        int[] arr = {1,3,4,3};

        int[] ans = new int[arr.length];

        Stack<Integer> st = new Stack<>();

        for (int i=arr.length-1;i >= 0;i--){
            while (st.size() > 0 && st.peek() < arr[i]){
                st.pop();
            }
            ans[i] = st.size()>0 ? st.peek() : -1;
            st.push(arr[i]);
        }

        for (int i =0;i< ans.length;i++){
            System.out.println(ans[i] + " ");
        }
    }
}
