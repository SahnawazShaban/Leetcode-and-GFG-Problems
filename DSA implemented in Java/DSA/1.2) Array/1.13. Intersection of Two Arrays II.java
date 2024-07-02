/*
350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
*/

// SOLUTION

class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        // Arrays.sort(nums1);
        // Arrays.sort(nums2);
        // int i=0, j=0, k=0;

        // int n1 = nums1.length, n2 = nums2.length;

        // while (i < n1 && j < n2){
        //     if(nums1[i] == nums2[j]){
        //         nums1[k++] = nums1[i];
        //         i++;
        //         j++;
        //     }
        //     else if(nums1[i] < nums2[j]){
        //         i++;
        //     }
        //     else{
        //         j++;
        //     }
        // }

        // return Arrays.copyOfRange(nums1, 0, k);
        // ----------------------------------------
        int arr[]=new int[1001];
        int ans[]=new int[1001];
        int count=0;
        for(int i:nums1){
            arr[i]++;
        }
        for(int i :nums2){
            if(arr[i]>0){
                ans[count++]=i;
                arr[i]--;
            }
        }
        return Arrays.copyOfRange(ans,0,count);
    }
}


// nums1 = [1,2,2,1], nums2 = [2,2]

// arr = [0,2,0,0,0,0,0,0,0,0...........]
// ans = [2,2]

// count = 2

// ------------------------------------------

// nums1 = [4,9,5], nums2 = [9,4,9,8,4]

// arr = [0,0,0,0,0,1,0,0,0,0,0,0,0,0,......]
// ans = [9,4]

// count = 0