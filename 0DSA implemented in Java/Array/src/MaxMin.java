public class MaxMin {
    public static void main(String[] args) {
        int[] arr = {2,7,1,4,9,8};

        int max = arr[0],min =arr[0];

        for (int i=0;i<arr.length;i++){
            if(arr[i]>max){
                max=arr[i];
            }

            if(arr[i]<min){
                min = arr[i];
            }
        }
        System.out.println("Maximum array is "+max);
        System.out.println("Minimum array is "+min);
    }
}
