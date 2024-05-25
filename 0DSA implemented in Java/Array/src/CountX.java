import java.util.Arrays;
import java.util.Scanner;

public class CountX {
    static int strictlyGreater(int[] arr, int x){
        int count = 0;
        for (int i=0;i<arr.length;i++){
            if (arr[i]>x){
                count++;
            }
        }
        return count;
    }
    static int firstOccurrence(int[] arr, int x){
        int ans = -1;

        for (int i=0;i<arr.length;i++){
            if (arr[i]==x){
                ans = i;
                break;
            }
        }
        return ans;
    }
    static int latOccurrence(int[] arr, int x){
//        int count = 0;
        int ans=-1;

        for(int i=0;i<arr.length;i++){
            if (arr[i] == x){
//                count++;
                ans = i;
            }
        }
        return ans;
    }
    static int countOccurrence(int[] arr, int x){
        int count = 0;

        for(int i=0;i<arr.length;i++){
            if (arr[i] == x){
                count++;
            }
        }
        return count;
    }
    public static void main(String[] args) {
//        int[] arr={4,3,5,2,6,1,2,2,8,2,0};
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a size of array : ");
        int n = sc.nextInt();
        int[] arr= new int[n];
        System.out.println("Enter "+n+" element : ");

        for (int i=0;i<arr.length;i++){
            arr[i] = sc.nextInt();
        }

        System.out.println("Enter value of x : ");
        int x = sc.nextInt();
        int ans=countOccurrence(arr,x);
        System.out.println("Count of X is "+ans);

        int ans1=latOccurrence(arr,x);
        System.out.println("Last Index of X is "+ans1);

        int ans2 = firstOccurrence(arr,x);
        System.out.println("First Occurrence of X is "+ans2);

        int ans3 = strictlyGreater(arr,x);
        System.out.println("Strictly Greater of x is "+ans3);
    }
}
