import java.util.Arrays;
import java.util.HashMap;
import java.util.TreeMap;

public class GetCommonElement {
    public static void main(String[] args) {
        int[] arr = {1,2,4,3,1,1,5,6,2};
        int[] arr1 = {4,1,5,1,1,6,7,2,5};

        TreeMap<Integer,Integer> map = new TreeMap<>();

        for (int val : arr){
            if (map.containsKey(val)){
                int of = map.get(val);
                int nf = of+1;
                map.put(val,nf);
            }
            else {
                map.put(val,1);
            }
        }

//        for (int val : map.keySet()){
//            int key = map.get(val);
//
//            System.out.println(val + " " + key);
//        }

        for (int val : arr1){
            if (map.containsKey(val)){
                System.out.print(val+" ");
            }
            map.remove(val);
        }
    }
}
