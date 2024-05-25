import java.util.Scanner;

public class FreqOfArray {
    static int[] freqArray(int[] arr){
        int[] freq=new int[100005];

        for (int i=1;i<arr.length;i++){
            freq[arr[i]] = freq[arr[i]] + 1;
        }
        return freq;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter size of array : ");
        int n=sc.nextInt();
        int[] arr=new int[n];

        System.out.println("Enter element : ");

        for (int i=0;i<arr.length;i++){
            arr[i] = sc.nextInt();
        }

        int[] ans = freqArray(arr);

        System.out.println("Enter query : ");
        int q=sc.nextInt();

        while (q>0){
            System.out.println("Enter your element to find :");
            int x=sc.nextInt();
            if (ans[x]>0){
                System.out.println(ans[x]);
            }
            else {
                System.out.println("NO");
            }
            q--;
        }

    }
}
