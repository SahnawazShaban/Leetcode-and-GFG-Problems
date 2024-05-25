import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class ReverseArrayListInGroup1 {
    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<>();

        arr.add(1);
        arr.add(2);
        arr.add(3);
        arr.add(4);
        arr.add(5);
//        arr.add(6);
        arr.add(7);
        arr.add(8);
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the value of k : ");
        int k = sc.nextInt();
        int n=arr.size();

        System.out.println("Before");
        for (int val : arr){
            System.out.print(val + " ");
        }

        for (int i=0;i<n;i+=k){
            int s=i;
            int e=Math.min(i+k-1,n-1);

            while (s<e){
                Collections.swap(arr,s++,e--);
            }
        }

        System.out.println();
        System.out.println("After");
        for (int val : arr){
            System.out.print(val + " ");
        }
    }
}
