public class Pyramid1 {
    public static void main(String[] args) {
        int n=5;

        int[] ans = {2,4,1,6,7};

        for (int i=1;i<= ans.length;i++){
            System.out.println("Index : " + i + "| Value : " + ans[i-1]);
        }
    }
}
