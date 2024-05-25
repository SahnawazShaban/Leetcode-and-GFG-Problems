import java.util.Scanner;

public class FindProSum {
    static void printArray(int[] arr){
        for (int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
    static int proSum(int[] arr){
        int ans=0;
        for (int i=0;i<arr.length;i++) {
            for (int j=i+1;j< arr.length;j++){
                ans = ans + arr[i]*arr[j];
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter how many number u want?");
        int n = sc.nextInt();
        int[] arr = new int[n];

        System.out.println("Enter "+n+" Elements : ");
        for (int i=0;i<arr.length;i++){
            arr[i] = sc.nextInt();
        }

        int pro = proSum(arr);
        printArray(arr);
        System.out.println("Ans : "+pro);
    }
}

// input : 1 2 3 4
// output : 1*2 + 1*3 + 1*4 + 2*3 + 2*4 + 3*4
