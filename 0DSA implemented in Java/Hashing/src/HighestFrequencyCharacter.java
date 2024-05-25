import java.util.HashMap;
import java.util.Map;

public class HighestFrequencyCharacter {
    public static void main(String[] args) {
        String str = "bbcdfbbbcqbbrb";

        HashMap<Character,Integer> map = new HashMap<>();

        for (int i=0;i<str.length();i++){
            char ch = str.charAt(i); // store 1 by 1 element
            // if (map.containsKey(ch)){ //if that key is inside 'map' then increase value by 1
            //     int oldFreq = map.get(ch); // store that value of key
            //     int newFreq = oldFreq + 1;
            //     map.put(ch,newFreq);
            // }
            // else {
            //     map.put(ch,1);
            // }

            map.put(ch, map.getOrDefault(ch,0)+1);
        }
        char maxCharFreq = str.charAt(0);
        for (Character key : map.keySet()){
            if (map.get(maxCharFreq) < map.get(key)){
                maxCharFreq = key;
            }
        }
        System.out.println(maxCharFreq);

        // print both <key, value>
        // for (Map.Entry<Character,Integer> item : map.entrySet()){ 
        //     System.out.println(item);
        // }
    }
}
