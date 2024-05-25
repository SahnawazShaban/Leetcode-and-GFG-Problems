import java.util.Stack;

public class CelebrityProblem {
    public static void main(String[] args) {
        //n x n matrix
        int[][] cel = {{0,0,1,1,1},{1,0,0,1,0},{1,0,0,1,0},{0,0,0,0,0},{0,1,0,1,0}};

        Stack<Integer> st = new Stack<>();

        for (int i=0;i<cel.length;i++){
            st.push(i);
        }

        while (st.size() >= 2){
            int i=st.pop();
            int j=st.pop();

            if (cel[i][j] == 1){
                // i knows j -> j is celebrity
                st.push(j);
            }
            else {
                // j knows i -> i is celebrity
                st.push(i);
            }
        }

        int last_ele = st.pop();

        for (int i=0;i< cel.length;i++){
            if (i != last_ele){
                if (cel[i][last_ele] == 0 || cel[last_ele][i] == 1){
                    System.out.println("None");
                    return;
                }
            }
        }
        System.out.println("Celebrity row is " + last_ele);
    }
}
