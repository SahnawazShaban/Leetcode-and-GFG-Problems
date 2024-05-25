public class SlidingWindowMaxSum {
    public static void main(String[] args) {
        int[] arr = {2,3,5,2,9,7,1};
        int sum=0,max=0;

        //brute force
//        for (int i=0;i< arr.length-2;i++){
//            sum = 0;
//            for (int j=i;j<i+3;j++){
//                sum += arr[j];
//            }
//            if(sum > max){
//                max = sum;
//            }
//        }
//        System.out.println(max);

        //better approach
        int j = 0,i = 0,k=3;

        while (j< arr.length){
            sum += arr[j];

            if(j-i+1 < k){
                j++;
            }
            else if (j-i+1 == k){
                if(sum > max){
                    max = sum;
                }
                sum -= arr[i];
                i++;
                j++;
            }
        }
        System.out.println(max);
    }
}
