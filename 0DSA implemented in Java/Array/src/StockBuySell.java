public class StockBuySell {
    public static void main(String[] args) {
        int[] prices = {7,1,4,5,3,6};
        int min_price = Integer.MAX_VALUE;
        int profit = 0;
        int max_profit = 0;

        for (int i=0;i<prices.length;i++){
            if (prices[i] < min_price){
                min_price = prices[i];
            }
            profit = prices[i]-min_price;

            if (max_profit < profit){
                max_profit = profit;
            }
        }

        System.out.println(max_profit);
    }
}
