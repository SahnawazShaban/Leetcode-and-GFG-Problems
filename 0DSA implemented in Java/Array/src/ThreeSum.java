import java.util.Scanner;

public class ThreeSum {
    static int firstRepeatingNumber(int[] arr){
        for (int i=0;i<arr.length;i++){
            for (int j=i+1;j<arr.length;j++){
                if (arr[i] == arr[j]){
                    return arr[i];
                }
            }
        }
        return -1;
    }
//    static int largestElement(int[] arr){
//        int maxi = Integer.MIN_VALUE;
//        for (int i=0;i<arr.length;i++){
//            if (arr[i]>maxi){
//                maxi=arr[i];
//            }
//        }
//        return maxi;
//    }
//
//    static int secondLargestElement(int[] arr){
//        int maxi = largestElement(arr);
//
//        for (int i=0;i<arr.length;i++){
//            if(arr[i] == maxi){
//                arr[i] = Integer.MIN_VALUE;
//            }
//        }
//        return largestElement(arr);
//    }

//    static int uniqueElement(int[] arr){
//        for (int i=0;i<arr.length;i++){
//            for (int j=i+1;j<arr.length;j++){
//                if (arr[i] == arr[j]){
//                    arr[i] = -1;
//                    arr[j] = -1;
//                }
//            }
//        }
//
//        int ans=-1;
//        for (int i=0;i<arr.length;i++){
//            if (arr[i]>ans){
//                ans=arr[i];
//            }
//        }
//        return ans;
//    }

//    static int threeSum(int[] arr,int target) {
//        int count = 0;
//        for (int i = 0; i < arr.length; i++) {
//            for (int j = i; j < arr.length; j++) {
//                for (int k = j; k<arr.length; k++) {
//                    if (arr[i] + arr[j] + arr[k] == target){
//                        count++;
//                        System.out.println(arr[i]+" "+arr[j]+" "+arr[k]);
//                    }
//                }
//            }
//        }
//        return count;
//    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter no. of element : ");
        int n = sc.nextInt();
        int[] arr = new int[n];

        System.out.println("Enter element : ");
        for (int i=0;i<arr.length;i++){
            arr[i]  = sc.nextInt();
        }

//        System.out.println("Enter target value :");
//        int target = sc.nextInt();

//        int ans = threeSum(arr,target);
//        System.out.println(ans);

//        int ans1 = uniqueElement(arr);
//        System.out.println("Unique Element is "+ans1);

//        int ans2 = secondLargestElement(arr);
//        System.out.println("Largest Element is "+ans2);

        int ans3 = firstRepeatingNumber(arr);
        System.out.println("First Repeating number is "+ans3);
    }
}
