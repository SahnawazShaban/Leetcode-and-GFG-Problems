import java.util.Scanner;

public class KthLargestElement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Kth Value : ");
        int k = sc.nextInt();
        int[] arr = {2,5,3,7,8,1,9};

        for (int i=0;i<arr.length-1;i++){
            for(int j=i+1;j<arr.length;j++){
                if (arr[i]<arr[j]){
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
            if(i == k-1){
                System.out.println(k+" Largest value is "+arr[i]);
                break;
            }
        }
    }
}
