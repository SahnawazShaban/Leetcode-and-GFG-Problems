public class ReverseNumber {
    public static int reverse(int x) {
        int digit=0, ans=0;
        while(x!=0){   //123!=0, 12!=0, 1!=0, 0!=0 (incorrect - > break the loop)
            digit=x%10;  //3, 2, 1

            if((ans > (Integer.MAX_VALUE/10)) || (ans < (Integer.MIN_VALUE/10))){
                return 0;
            }

            ans=ans*10+digit; //3, 32, 321
            x=x/10; //12, 1, 0 (0 - > i click the while loop condition)
        }
        return ans;
    }
    public static void main(String[] args) {
        int x=-123;

        int ans = reverse(x);

        System.out.println(ans);
    }
}
