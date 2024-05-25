public class FindDuplicateElement {
    static void printArray(int[] arr){
        for (int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] arr= {3,2,1,6,2,1};
        System.out.println("Enter element : ");
        int n=arr.length;
        int[] ans = new int[n];
        int k=0;

        System.out.println("Before");
        printArray(arr);

        for (int i=0;i<arr.length;i++){
            for (int j=i+1;j<arr.length;j++){
                if (arr[i] == arr[j]){
                    ans[k++] = arr[i];
                }
            }
        }

        System.out.println("After");
        printArray(ans);
    }
}


//input : [3,2,1,6,2,1]
//output : [2,1]