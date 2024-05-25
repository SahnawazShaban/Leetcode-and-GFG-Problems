import java.util.HashMap;
import java.util.Scanner;

public class TwoSum {
    public static void main(String[] args) {
        //[2,7,11,15] and target = 9
        //return arr with, [target-nums, current value index]
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter value of array : ");
        int n = sc.nextInt();
        int[] arr = new int[2];
        int[] numbers = new int[n];

        for (int i=0;i<numbers.length;i++){
            numbers[i] = sc.nextInt();
        }

        System.out.println("Enter value of target : ");
        int target = sc.nextInt();
        HashMap<Integer,Integer> map = new HashMap<>();

        for (int i=0;i<numbers.length;i++){
            if (map.containsKey(target - numbers[i])){
                arr[1] = i;
                arr[0] = map.get(target-numbers[i]);
                System.out.println("[" + arr[0] + "," + arr[1] + "]");
            }
            map.put(numbers[i],i);
        }
//        System.out.println("[" + arr[0] + "," + arr[1] + "]");
    }
}
