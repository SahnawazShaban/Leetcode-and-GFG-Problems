import java.util.Scanner;
public class SearchIndex {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter key : ");
        int key = sc.nextInt();
        int[] arr = {2,6,7,3,5,9,11};
        int ans = -1;

        for (int i=0;i<arr.length;i++){
            if(key == arr[i]) {
                ans = i;
                System.out.println("Index of "+arr[i]+" is "+ans);
                break;
            }
        }
        System.out.println(ans);
    }
}
