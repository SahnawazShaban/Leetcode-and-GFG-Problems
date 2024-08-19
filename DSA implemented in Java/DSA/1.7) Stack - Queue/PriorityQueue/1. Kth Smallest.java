/*
Kth Smallest
Difficulty: Medium
Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the kth smallest element in the given array. It is given that all array elements are distinct.

Follow up: Don't solve it using the inbuilt sort function.

Examples :
Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output:  7
Explanation: 3rd smallest element in the given array is 7.

Input: arr[] = [7, 10, 4, 20, 15], k = 4 
Output:  15
Explanation: 4th smallest element in the given array is 15.


Expected Time Complexity: O(n+(max_element) )
Expected Auxiliary Space: O(max_element)

Constraints:
1 <= arr.size <= 10^6
1<= arr[i] <= 10^6
1 <= k <= n

Seen this question in a real interview before ?
Yes
No
Company Tags
VMWare, Accolite, Amazon, Microsoft, Snapdeal, Hike, Adobe, Google, ABCO, Cisco
*/

// SOLUTION

class Solution {
    public static int kthSmallest(int[] arr, int k) {
        int n = arr.length;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int i = 0;
        
        while(i < k){
            pq.add(-arr[i++]);
        }
        
        while(i < n){
            pq.add(-arr[i++]);
            
            if(pq.size() > k){
                pq.poll();
            }
        }
        
        return -pq.peek();
    }
}