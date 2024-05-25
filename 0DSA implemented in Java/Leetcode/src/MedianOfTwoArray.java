import java.util.Arrays;

public class MedianOfTwoArray {
    public static void mergeArray(int[] nums1,int[] nums2,int n1, int n2, int[] arr){
        int i=0,j=0,k=0;

        while (i<n1 && j<n2){
            if (nums1[i] < nums2[j]){
                arr[k++] = nums1[i++];
            } else if (nums2[j] < nums1[i]) {
                arr[k++] = nums2[j++];
            }
            else {
                arr[k++] = nums1[i++];
            }
        }

        while (i<n1){
            arr[k++] = nums2[i++];
        }

        while (j<n2){
            arr[k++] = nums2[j++];
        }
    }

//    public static void mergeArray(int[] nums1,int[] nums2,int n1, int n2, int[] arr){
//        int i=0,j=0,k=0;
//
//        while (i<n1){
//            arr[k++] = nums1[i++];
//        }
//
//        while (j<n2){
//            arr[k++] = nums2[j++];
//        }
//
//        Arrays.sort(arr);
//    }
    public static void main(String[] args) {
        int[] nums1 = {1,3};
        int[] nums2 = {2,6};

        int n1 = nums1.length;
        int n2 = nums2.length;

        int n = n1+n2;

        int[] arr = new int[n];

        mergeArray(nums1,nums2,n1,n2,arr);

        System.out.println("ANS : Without using inbuilt sort function - ");

        for (int i=0;i<n;i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();




        //merge array
//        int[] nums1 = {1,3};
//        int[] nums2 = {2,6};
//        int n = nums1.length + nums2.length - 1;
//
//        int i = nums1.length;
//        int j = nums2.length;
//
//        int ans = i+j;
//
//        int[] arr = new int[ans];
//
//        System.arraycopy(nums1,0,arr,0,i);
//        System.arraycopy(nums2,0,arr,i,j);
//
//        System.out.println(Arrays.toString(arr));


    }
}
