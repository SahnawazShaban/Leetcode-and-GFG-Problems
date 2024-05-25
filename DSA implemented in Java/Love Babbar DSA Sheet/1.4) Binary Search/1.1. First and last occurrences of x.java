/*
First and last occurrences of x
Medium
Given a sorted array arr containing n elements with possibly some duplicate, the task is to find the first and last occurrences of an element x in the given array.
Note: If the number x is not found in the array then return both the indices as -1.

Example 1:
Input:
n=9, x=5
arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
Output:  
2 5
Explanation: 
First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5. 

Example 2:
Input:
n=9, x=7
arr[] = { 1, 3, 5, 5, 5, 5, 7, 123, 125 }
Output:  
6 6
Explanation: 
First and last occurrence of 7 is at index 6.
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function find() that takes array arr, integer n and integer x as parameters and returns the required answer.

Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 10^6
1 ≤ arr[i],x ≤ 10^9
*/

// SOLUTION

class GFG
{
    ArrayList<Integer> find(int arr[], int n, int x)
    {
        /*
        ArrayList<Integer> list = new ArrayList<>();
        int left = 0, right = n-1;
        list.add(-1);
        list.add(-1);
             
        while(left <= right) {
            if(arr[left] == x && arr[right] == x) {
                list.add(0,left);
                list.add(1,right);
                break;
            }
            if(arr[left] != x ) left++;
            
            if(arr[right] != x ) right--;
         }
        return list;
        */
        
        /*
        for(int i=0 ; i<n ; i++){
            if(x==arr[i]) ans.push_back(i);
        }
        
        Collections.sort(ans);
        if(!ans.empty()){
            return{ans[0], ans[ans.size()-1]};
        }
        return{-1, -1};
        */
        
        ArrayList<Integer> ans = new ArrayList<>();
        
        int startIdx = firstOcc(arr, n, x);
        int endIdx = lastOcc(arr, n, x);
        
        ans.add(startIdx);
        ans.add(endIdx);
        
        return ans;
        
    }
    
    int firstOcc(int arr[], int n, int x){
        int s = 0;
        int e = n-1;
        int mid = s + (e - s)/2;
        
        int idx = -1;
        
        while (s <= e){
            if (arr[mid] == x){
                idx = mid;
                e = mid-1;
            }
            else if (arr[mid] > x){
                e = mid-1;
            }
            else{
                s = mid+1;
            }
            mid = s + (e - s)/2;
        }
        return idx;
    }
    
    int lastOcc(int arr[], int n, int x){
        int s = 0;
        int e = n-1;
        int mid = s + (e - s)/2;
        
        int idx = -1;
        
        while (s <= e){
            if (arr[mid] == x){
                idx = mid;
                s = mid+1;
            }
            else if (arr[mid] > x){
                e = mid-1;
            }
            else{
                s = mid+1;
            }
            mid = s + (e - s)/2;
        }
        return idx;
    }
}
