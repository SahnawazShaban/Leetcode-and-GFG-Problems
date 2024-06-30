/*
Example 1:
Input: items = ["item1", "item2", "item3", "item1", "item3"]
Output: ["item3", "item1", "item2"]
*/


//Solution

// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.*;

class HelloWorld {
    public static ArrayList<String> getRecentRequest(String[] items, ArrayList<String> ans){
        int n = items.length;
        if(n == 0){
            return ans;
        }
        
        Map<String, Boolean> map = new HashMap<>();
        
        for (int i = n-1; i>=0; i--){
            if(!map.containsKey(items[i])){
                ans.add(items[i]);
                map.put(items[i], true);
            }
        }
        
        return ans;
    }
    
    public static void main(String[] args) {
        String[] items = {"item1", "item2", "item3", "item1", "item3"};
        
        ArrayList<String> ans = new ArrayList<>();
        getRecentRequest(items, ans);
        
        for(String item : ans){
            System.out.println(item);
        }
    }
}