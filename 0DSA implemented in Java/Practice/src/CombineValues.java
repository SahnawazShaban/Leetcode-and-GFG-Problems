import java.lang.Math;
public class CombineValues {
    static void printArray(int[] arr){
        for (int i=0;i<arr.length;i++){
            System.out.print(arr[i]+"");
        }
        System.out.println();
    }
    static void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    public static void main(String[] args) {
        int[] arr = {2,4,9,3,1,0};
        int n = arr.length;
        int ans = 0,i=0,j=arr.length-1;

//        while (n!=0){
//            ans = (int) (arr[i]+ans*10);
//            n--;
//            i++;
//        }
//        System.out.println(ans);

        printArray(arr);
        while(i<=j){
            swap(arr,i,j);
            i++;
            j--;
        }

        printArray(arr);
    }
}
