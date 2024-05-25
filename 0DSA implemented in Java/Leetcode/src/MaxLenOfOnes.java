public class MaxLenOfOnes {
    public static void main(String[] args) {
        int[] arr = {1,0,0,1,1,0,1,0,1,1,1,1};
        int j=0;
        int k=1; // for how many 0 is occurs
        int ans=0;
        for (int i=0;i<arr.length;i++){

            if (arr[i] == 0){
                k--;
            }

            while (k < 0){
                if (arr[j] == 0){
                    k++;
                }
                j++;
            }
            //if have to revert '0 to 1', only 1 time, then i have to add '+1' after 'i-j'
            //if I skip this '0' then don't write '+1'
            ans = Math.max(ans,i-j+1);
        }

        System.out.println(ans);
    }
}
