import java.util.HashMap;

public class GetCommonElement2 {
    public static void main(String[] args) {
        int[] arr = {1,2,4,3,1,5,6,2};
        int[] arr1 = {4,1,5,1,1,6,7,2,5,4};

        HashMap<Integer,Integer> map = new HashMap<>();

        for (int val:arr){
            if (map.containsKey(val)){
                int of = map.get(val);
                int nf = of+1;
                map.put(val,nf);
            }
            else {
                map.put(val,1);
            }
        }

        for (int val:arr1){
            if (map.containsKey(val) && map.get(val) > 0){
                System.out.print(val + " ");
                int of = map.get(val);
                int nf = of-1;
                map.put(val,nf);
            }
        }
    }
}
