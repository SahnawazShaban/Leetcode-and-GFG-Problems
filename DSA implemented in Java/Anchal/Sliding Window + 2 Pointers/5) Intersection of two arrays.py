"""
Intersection of two arrays

Easy

Given two arrays a[] and b[] respectively of size n and m, the task is to print the count of elements in the intersection (or common elements) of the two arrays.

For this question, the intersection of two arrays can be defined as the set containing distinct common elements between the two arrays. 

Example 1:
Input:
n = 5, m = 3
a[] = {89, 24, 75, 11, 23}
b[] = {89, 2, 4}
Output: 1
Explanation: 
89 is the only element 
in the intersection of two arrays.

Example 2:
Input:
n = 6, m = 5
a[] = {1, 2, 3, 4, 5, 6}
b[] = {3, 4, 5, 6, 7} 
Output: 4
Explanation: 
3 4 5 and 6 are the elements 
in the intersection of two arrays.
Your Task:
You don't need to read input or print anything. Your task is to complete the function NumberofElementsInIntersection() which takes two integers n and m and their respective arrays a[] and b[]  as input. The function should return the count of the number of elements in the intersection.

 
Expected Time Complexity: O(n + m).
Expected Auxiliary Space: O(min(n,m)).

Constraints:
1 ≤ n, m ≤ 10^5
1 ≤ a[i], b[i] ≤ 10^5

"""

# SOLUTION

#Function to return the count of the number of elements in
#the intersection of two arrays.
class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
        set_b = set(b)
        count = 0
    
        i = 0
        while i < n:
            if a[i] in set_b:
                count += 1
                set_b.remove(a[i])
            i += 1
    
        return count
        
        '''
        Time Complexity:

        Constructing the set set_b from array b has a time complexity of O(m), where m is the length of array b.
        The while loop iterates through the array a once. Inside the loop, the in operation and the remove operation both have an average time complexity of O(1) for sets.
        Overall, the time complexity is O(m + n).
        
        Space Complexity:

        The space complexity is O(m) due to the set set_b constructed from array b.
        '''
        # --------------------------------------
        
        set_a = set(a)
        set_b = set(b)
        
        intersection = set_a.intersection(set_b)
        
        # ------------------------------------
        
        # TLE
        '''
        a.sort()
        b.sort()
        
        i, j = 0, 0
        count = 0
        
        while i < n and j < m:
            if a[i] == b[j]:
                count += 1
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
                
        return count
        '''
        
        # -------------------------------
        
        # TLE
        '''
        set_a = set(a)
        count = 0
    
        for i in range(m):
            if b[i] in set_a:
                count += 1
    
        return count
        '''
        # ---------------------------
        
        '''
        count = 0
        unique_elements = set()
    
        for element in a:
            unique_elements.add(element)
    
        for element in b:
            if element in unique_elements:
                count += 1
                unique_elements.remove(element)
    
        return count
        '''