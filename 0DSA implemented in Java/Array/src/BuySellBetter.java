public class BuySellBetter {
    public static void main(String[] args) {
        int[] stock_price = {3,5,1,7,4,9,3};
        int profit=0;

        for (int i=1;i<stock_price.length;i++){
            if (stock_price[i]>stock_price[i-1]){
                profit = (stock_price[i] - stock_price[i-1]);
            }
        }
        System.out.println(profit);
    }
}
//3 -> 5 = 2
//1 -> 7 = 6
//4 -> 9 = 5
//
//2+6+9 = 13
