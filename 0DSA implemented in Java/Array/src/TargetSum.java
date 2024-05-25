public class TargetSum {
    public static void main(String[] args) {
        int[] arr = {4,6,3,5,8,2};
        int count = 0;

        for (int i=0;i<arr.length;i++){
            for (int j=i;j<arr.length;j++){
                if (arr[i]+arr[j] == 7){
                    count++;
                    System.out.println("("+arr[i] + " , " + arr[j]+")");
                }
            }
        }
        System.out.println("Total pair is "+count);
    }
}
