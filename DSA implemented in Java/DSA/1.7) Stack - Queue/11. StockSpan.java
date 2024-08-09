/* 
Input 1:
arr = {2, 5, 3, 8, 9, 7, 1, 2}
Output:
1 2 1 4 5 1 1 2

Input 2:
arr = {10, 4, 5, 90, 120, 80}
Output:
1 1 2 4 5 1
*/

import java.util.Stack;

public class StockSpan {
    public static void main(String[] args) {
        int[] arr = {2,5,3,8,9,7,1,2};

        Stack<Integer> st = new Stack<>();
        st.push(0);

        int[] span = new int[arr.length];

        span[0] = 1;

        for (int i=1;i<arr.length;i++){
            while (st.size() > 0 && arr[i] > arr[st.peek()]){
                st.pop();
            }

            if (st.size() == 0){
                span[i] = i+1;
            }
            else {
                span[i] = i - st.peek();
            }

            st.push(i);
        }

        for (int i=0;i<arr.length;i++){
            System.out.println(span[i] + " ");
        }
    }
}
