public class Decimal2Binary {
    public static void main(String[] args) {
//        intput : 14
//        output : 1110

        int num = 32, i=0;
        int ans = 0;

        while (num !=0){
            int bit = num&1;
            ans = ans+bit*(int)Math.pow(10,i);
            num = num >> 1;
            i++;
        }
        System.out.println(ans);
    }
}
