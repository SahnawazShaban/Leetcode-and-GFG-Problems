import java.util.HashMap;

public class LongestConsecutiveSequence {
    public static void main(String[] args) {
        int[] arr = {100,4,200,1,2,3,5,102,103,8,104,105};

        HashMap<Integer,Boolean> map = new HashMap<>();

        for (int val : arr){
            map.put(val,true);
        }

        for (int val : arr){
            if (map.containsKey(val-1)){
                map.put(val,false);
            }
        }

        int maxLen = 0;
        for (int val : arr){
            if (map.get(val) == true){
                int tempLen = 1;
                int tempStartPoint = val;

                System.out.println("TSP : "+ tempStartPoint);
                while (map.containsKey(tempStartPoint+tempLen)){
                    tempLen++;
                    System.out.println("TL : "+tempLen);
                }

                System.out.println("Before ML : " + maxLen);
                if (tempLen > maxLen){
                    maxLen = tempLen;
                }
                System.out.println("After ML : " + maxLen);
            }
        }
        System.out.println(maxLen);
    }
}
