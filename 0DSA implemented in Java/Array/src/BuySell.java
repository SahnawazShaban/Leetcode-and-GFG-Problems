public class BuySell {
    public static void main(String[] args) {
        int[] stock_price = {3,5,1,7,4,9,3};
        int profit = 0;
        int max_profit = 0;

        for (int i=0;i<stock_price.length;i++){
            for (int j=i+1;j<stock_price.length;j++){
                if (stock_price[i] < stock_price[j]){
                    profit = stock_price[j] - stock_price[i];

                    if (profit > max_profit){
                        max_profit = profit;
                    }
                }
            }
        }
        System.out.println(max_profit);
    }
}
