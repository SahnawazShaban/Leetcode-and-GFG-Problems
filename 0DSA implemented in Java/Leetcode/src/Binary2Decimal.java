public class Binary2Decimal {
    public static void main(String[] args) {
        int n=1110;
        int ans=0,i=0;

        while (n != 0){
            int digit = n%10;
            ans = ans+digit*(int)Math.pow(2,i);
            n = n/10;
            i++;
        }
        System.out.println(ans);
    }
}
