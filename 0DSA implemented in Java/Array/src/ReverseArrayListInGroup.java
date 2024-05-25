import java.util.ArrayList;
import java.util.Collections;

public class ReverseArrayListInGroup {
    public static void swap(ArrayList<Integer> arr, int l, int r){
        while (l<r){
            Collections.swap(arr,l,r);
            l++;
            r--;
        }
    }
    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<>();

        arr.add(1);
        arr.add(2);
        arr.add(3);
        arr.add(4);
        arr.add(5);
        arr.add(6);
        arr.add(7);
        arr.add(8);
        int k=2;
        int i;
        int n=arr.size();
        for (i=0;i+k<n;i+=k){
            int l=i;
            int r=i+k-1;

            swap(arr,l,r);
        }

        if (i+k != n-1){
            swap(arr,i,n-1);
        }

        for (int val : arr){
            System.out.print(val + " ");
        }
    }
}
