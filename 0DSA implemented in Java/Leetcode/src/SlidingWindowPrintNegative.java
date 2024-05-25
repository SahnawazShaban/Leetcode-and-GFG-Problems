public class SlidingWindowPrintNegative {
    public static void main(String[] args) {
       int[] arr = {2,3,1,5,6,3};

       int j=0,i=0,k=3,sum=0,max=0;

       while (j< arr.length){
           sum += arr[j];

           if (j-i+1 < k){
               j++;
           } else if (j-i+1 == k) {
               if (sum > max){
                   max = sum;
               }
               sum = sum - arr[i];

               i++;
               j++;
           }
       }
        System.out.println(max);
    }
}
