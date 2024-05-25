public class ReverseArrayInGroup {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};
        int n= arr.length;
        int[] arr1 = new int[n];

        int k=2;
        int j=0;

        for (int i=k-1;i>=0;i--){
            arr1[j++] = arr[i];
        }

        for (int i=n-1;i>=k;i--){
            arr1[j++] = arr[i];
        }

        for (int val : arr1){
            System.out.print(val + " ");
        }
    }
}
