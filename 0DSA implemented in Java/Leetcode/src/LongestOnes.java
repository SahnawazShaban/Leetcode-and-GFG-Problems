public class LongestOnes {
    public static void main(String[] args) {
        //Longest One's - you have to flip '2' 0's to 1.
        int[] arr = {1,1,0,1,0,1,1,1,1,0,0,0,0,1,1,1};

        int j=0; // slow pointer
        int k=2; // sliding window
        int ans = 0;

        for (int i=0;i< arr.length;i++){
            if(arr[i] == 0){
                k--;
            }
            while (k<0){
                if (arr[j] == 0){
                    k++;
                }
                j++;
            }
            ans = Math.max(ans,i-j+1);
        }
        System.out.println(ans);
    }
}
