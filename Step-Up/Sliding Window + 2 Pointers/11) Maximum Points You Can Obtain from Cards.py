"""
1423. Maximum Points You Can Obtain from Cards

Medium

There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.


Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
 

Constraints:

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length

"""

# SOLUTION

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Solution - 1
        # time: O(n), space: O(1)

        # size = len(cardPoints) - k
        # S = sum(cardPoints[size:])
        # ans = S
        # for i in range(0, k):
        #     S += cardPoints[i]
        #     S -= cardPoints[i+size]
        #     ans = max(ans, S)
        
        # return ans

        # ------------------------------------

        # Solution - 2
        '''
        maxScore = 0
        n = len(cardPoints)

        for i in range(k + 1):
            frontSum = sum(cardPoints[:i])
            backSum = sum(cardPoints[n - k + i:])
            maxScore = max(maxScore, frontSum + backSum)

        return maxScore
        '''

        '''
        Time Complexity:
        The outer loop runs k + 1 times, and for each iteration, there are two calls to the sum function. The sum function has a time complexity of O(n) where n is the length of cardPoints.
        Therefore, the overall time complexity is O((k + 1) * 2n) = O(kn).

        Space Complexity:
        The space complexity is determined by the space used for the variables maxScore, n, i, frontSum, and backSum.
        The dominant factor is the frontSum and backSum arrays, each with a maximum length of k + 1. Therefore, the space complexity is O(k).
        '''
        # ------------------------------------
        # Solution - 3
        '''
        n = len(cardPoints)
        totalSum = sum(cardPoints)
        windowSize = n - k
        currentSum = sum(cardPoints[:windowSize])
        minSum = currentSum

        for i in range(windowSize, n):
            currentSum += cardPoints[i] - cardPoints[i - windowSize]
            minSum = min(minSum, currentSum)

        return totalSum - minSum
        '''

        # ---------------------------------------

        # Solution - 4

        frontSum, backSum = [0], [0]
    
        # Calculate the prefix sum from the front
        for n in cardPoints:
            frontSum.append(frontSum[-1] + n)

        # Calculate the prefix sum from the back
        for n in cardPoints[::-1]: 
            backSum.append(backSum[-1] + n)

        # Calculate the maximum score for each combination
        allCombinations = [frontSum[i] + backSum[k-i] for i in range(k + 1)]

        # Return the maximum score
        return max(allCombinations)

        '''
        # [1, 2, 3, 4, 5, 6, 1]
        # n = 7 and k = 3, n-k = 4 (window size)

        # [(1, 2, 3, 4), 5, 6, 1] -> (5+6+1)(r) = 12
        # [1, (2, 3, 4, 5), 6, 1] -> (1)(l) + (6+1)(r) = 8
        # [1, 2, (3, 4, 5, 6), 1] -> (1,2)(l) + (1)(r) = 4
        # [1, 2, 3, (4, 5, 6, 1)] -> (1,2,3)(l) = 6

        # max(12,8,4,6) = 12

        That's why we use prefix sum (frontSum and backSum)
        '''

        '''
        Time Complexity:
        The first loop that calculates the prefix sum from the front iterates through each element in cardPoints. This has a time complexity of O(N), where N is the number of elements in cardPoints.
        The second loop that calculates the prefix sum from the back also iterates through each element in cardPoints. This also has a time complexity of O(N).
        Reversing the backSum list has a time complexity of O(N).
        The loop that calculates the maximum score for each combination iterates k + 1 times. Since k can be at most equal to the length of cardPoints, the time complexity of this loop is O(N).
        The overall time complexity is dominated by the linear iterations through cardPoints, making it O(N).

        Space Complexity:
        Two lists, frontSum and backSum, are used to store the prefix sums. Both have a length of N + 1, where N is the number of elements in cardPoints. Therefore, the space complexity for these lists is O(N).
        The allCombinations list also has a length of k + 1, so its space complexity is O(k).
        The overall space complexity is O(N) due to the prefix sum lists.

        In summary, the time complexity is O(N), and the space complexity is O(N).
        '''

'''
IMPORTANT NOTE : 

- Choose exactly k cards from this list of cards but only one trick is that,
Suppose k = 3, (we want 3 cards we could either choose all 3 cards from the left
and none from the right) or (we could choose 2 cards from the left and 1 from the right)
or (we could choose no cards from the left and 3 cards from the right).
'''

'''
I intentionally kept the print statements for easier understanding. Here is the output:
cardPoints: [1, 2, 3, 4, 5, 6, 1]
k: 3
frontSum: [0, 1]
frontSum: [0, 1, 3]
frontSum: [0, 1, 3, 6]
frontSum: [0, 1, 3, 6, 10]
frontSum: [0, 1, 3, 6, 10, 15]
frontSum: [0, 1, 3, 6, 10, 15, 21]
frontSum: [0, 1, 3, 6, 10, 15, 21, 22]
backSum : [0, 1]
backSum : [0, 1, 7]
backSum : [0, 1, 7, 12]
backSum : [0, 1, 7, 12, 16]
backSum : [0, 1, 7, 12, 16, 19]
backSum : [0, 1, 7, 12, 16, 19, 21]
backSum : [0, 1, 7, 12, 16, 19, 21, 22]
allCombinations: [12, 8, 4, 6]
'''
