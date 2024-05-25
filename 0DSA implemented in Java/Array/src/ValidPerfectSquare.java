public class ValidPerfectSquare {
    public static boolean isPerfectSquare(int num) {
        if(num < 1){
            return false;  // edge case
        }
        long start = 1, end = num;

        while(start <= end){
            long mid = start + (end - start)/2;

            long ans = mid * mid;

            if(ans > num){
                end = mid-1;
            }
            else if(ans < num){
                start = mid+1;
            }
            else{
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int n=16;
        boolean ans = isPerfectSquare(n);
        System.out.println(ans);
    }
}
