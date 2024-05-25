public class BuySell {
    public static void main(String[] args) {
        int[] prices = {3,5,1,7,4,9,3};
        int n=prices.length;
        int[] temp = new int[n];
        int extra = 0;

        for (int i=n-1;i>=1;i--){
            if (prices[i]>prices[i-1]){
                extra = prices[i];
            }
            temp[i] = extra;
        }

        for (int i=0;i<temp.length;i++){
            System.out.print(temp[i]+" ");
        }

    }
}
