/*
1636. Sort Array by Increasing Frequency
Easy
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

Example 1:
Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Example 2:
Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

Example 3:
Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
*/


// SOLUTION

class Solution {
    public int[] frequencySort(int[] nums) {
        int n = nums.length;
        Map<Integer, Integer> map = new HashMap<>();

        for (int val : nums){
            map.put(val, map.getOrDefault(val, 0)+1);
        }

        List<Integer> list = new ArrayList<>(map.keySet());
        Collections.sort(list, (a,b) -> {
            return (map.get(a) == map.get(b)) ? b-a : map.get(a) - map.get(b);
        });

        int[] res = new int[n];
        int j = 0;
        for(int num : list){
            for(int i = 0; i < map.get(num); i++){
                res[j++] = num;
            }
        }
        return res;
    }
}

/*
public int[] frequencySort(int[] nums) {
    Map<Integer, Integer> map = new HashMap<>();
    List<Integer> ans = new ArrayList<>();
    for (int n : nums) {                            
        ans.add(n);
        map.put(n, map.getOrDefault(n, 0) + 1);
    }

    Collections.sort(ans, (a, b) ->                 
        (map.get(a) == map.get(b))? b - a : map.get(a) - map.get(b)
    );

    return ans.stream().mapToInt(i -> i).toArray(); // O(n)
}

ans.stream().mapToInt(i -> i).toArray();

ans.stream(): This converts the ans list (which contains Integer objects) into a stream of Integer elements.
.mapToInt(i -> i): The mapToInt operation maps each element from the stream to an int. In this case, it converts each Integer to its corresponding primitive int value.
.toArray(): Finally, this converts the resulting IntStream back into an int[] array.
*/

// List<Integer> list = new ArrayList<>(Arrays.asList(5, 7, 3));
// list.sort((a, b) -> a.compareTo(b)); // Sort in ascending order
// // Alternatively, you can use: list.sort(Comparator.naturalOrder());

// for (int x : list) {
//     System.out.print(x + " ");
// }
// // Output: 3 5 7

// asList method is part of the java.util.Arrays class in Java. It allows you to convert an array into a List


// Thus, b - a is used to ensure that when the frequency is the same, the larger number (b) comes before the smaller number (a).