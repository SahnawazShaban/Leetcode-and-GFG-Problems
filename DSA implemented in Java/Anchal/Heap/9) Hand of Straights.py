"""
846. Hand of Straights

Medium

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
 

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

 

Constraints:

1 <= hand.length <= 10^4
0 <= hand[i] <= 10^9
1 <= groupSize <= hand.length
 

Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

"""

# SOLUTION

import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Get the length of the hand
        n = len(hand)

        # If the length is not divisible by groupSize, it's impossible to split the hand
        if n % groupSize:
            return False

        # Create a dictionary to count the occurrences of each value in the hand
        temp_dict = {}
        for val in hand:
            temp_dict[val] = temp_dict.get(val, 0) + 1

        # Create a min heap to keep track of the unique values in ascending order
        minh = []
        for key in temp_dict.keys():
            heapq.heappush(minh, key)

        # Iterate through the min heap
        while minh:
            # Get the first element in the min heap
            first = minh[0]

            # Iterate over the group of consecutive values
            for i in range(first, first + groupSize):
                # If the current value is not in the dictionary, it's impossible to split the hand
                if i not in temp_dict:
                    return False

                # Decrease the count of the current value
                temp_dict[i] -= 1

                # If the count becomes zero, remove the value from the min heap
                if temp_dict[i] == 0:
                    # Check if the value to be removed is the first in the min heap
                    if i != minh[0]:
                        return False
                    heapq.heappop(minh)

        # If all groups are successfully formed, return True
        return True

'''
Time Complexity:

The initial loop that creates the temp_dict takes O(n) time, where n is the length of the hand.
The second loop that creates the min heap has a time complexity of O(k log k), where k is the number of unique values in the hand.
The main while loop iterates through all unique values in the min heap, and for each value, it may iterate up to groupSize times. In the worst case, this results in O(n * groupSize) iterations.
Therefore, the overall time complexity is O(n + k log k + n * groupSize), but the dominant factor is the last term, so we can simplify it to O(n * groupSize).


Space Complexity:

The temp_dict dictionary stores the count of each unique value in the hand. In the worst case, there can be k unique values, so the space complexity for temp_dict is O(k).
The min heap (minh) also stores at most k unique values, resulting in a space complexity of O(k).
Therefore, the overall space complexity is O(k).
'''
