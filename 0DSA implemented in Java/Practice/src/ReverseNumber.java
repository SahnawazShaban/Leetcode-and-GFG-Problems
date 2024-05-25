import java.lang.Math;
public class ReverseNumber {
    public static void main(String[] args) {
        int n=12354461;
        int ans=0;

        while (n!=0){
            int rev=n%10;
            ans = rev+ans*10;
            n=n/10;
        }
        System.out.println(ans);
    }
}
