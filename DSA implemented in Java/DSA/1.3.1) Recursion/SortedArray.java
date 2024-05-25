public class SortedArray {
    public static boolean isSorted(int[] arr,int idx){
        if (idx == arr.length-1){
            return true;
        }
        if(arr[idx] < arr[idx+1]){
            //array is sorted
            return isSorted(arr,idx+1);
        }
        else {
            //array is not sorted
            return false;
        }
    }
    public static void main(String[] args) {
        int[] arr = {1,4,6,8,9};

        boolean ans = isSorted(arr,0);
        System.out.println(ans);
    }
}
