public class SlidingWindowMax {
    public static void main(String[] args) {
        int[] arr = {2,9,3,8,1,7,12,6,14,4,32,0,7,19,8,12,6};

        int k = 4, j,max,x=0;

        int[] ans = new int[arr.length];

        // we can't found last 3 index of max because value of k is 4, we just
        //found maximum of last 4 elements. (arr.length - k)
        for (int i=0;i< arr.length-k;i++){
            max = Integer.MIN_VALUE;
            //its goes to i - i+k
            for (j=i;j<i+k;j++){

                // found max of every current element and previous element
                max = Math.max(arr[j],max);
            }
            // x is store max and increment by 1
            // and store each value of max into 'ans' ARRAY.
            ans[x++] = max;
        }

        // if we don't write 'ans.length - k' then its replacement with '0' of remaining index
        for (int i=0;i< ans.length-k;i++){
            System.out.println(ans[i] + " ");
        }
    }
}
