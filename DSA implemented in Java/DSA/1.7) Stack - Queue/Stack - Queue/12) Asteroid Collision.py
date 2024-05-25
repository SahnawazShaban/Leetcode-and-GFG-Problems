"""
735. Asteroid Collision

Medium

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 
Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 10^4
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0

"""

# SOLUTION

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []

        # Iterate through each asteroid
        for i in range(n):
            # Check if the current asteroid is moving to the right or if the stack is empty
            if asteroids[i] > 0 or len(stack) == 0:
                # If conditions are met, push the asteroid onto the stack
                stack.append(asteroids[i])
            else:
                # Simulate asteroid collision when the current asteroid is moving to the left
                while len(stack) > 0 and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):
                    # Pop smaller asteroids until a larger or equal-sized one is encountered
                    stack.pop()

                # Check for equal-sized asteroids, destroy both
                if len(stack) > 0 and stack[-1] == abs(asteroids[i]):
                    stack.pop()
                else:
                    # If no larger asteroid is encountered or the stack is empty, push the current asteroid onto the stack
                    if len(stack) == 0 or stack[-1] < 0:
                        stack.append(asteroids[i])

        # Return the stack containing surviving asteroids after collisions
        return stack
    

        '''
        Time Complexity:
        The time complexity is O(n), where n is the length of the input list asteroids. Each asteroid is processed once.

        Space Complexity:
        The space complexity is O(n), where n is the length of the input list asteroids. In the worst case, all asteroids may be stored in the stack.
        '''

        # -----------------------------------------

        # Soution - 2

        stack = []
        for a in asteroids:
            # while stack is not empty and stack[-1] moves left and a moves right
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] + a == 0: # both collide
                    stack.pop()
                    break
                elif stack[-1] + a < 0: # previous a collide
                    stack.pop()
                else: # a collide
                    break
            # if while condition is false, execute else statement
            # if while break, do not execute else statement 
            else: 
                stack.append(a)
        return stack

        # ---------------------------------------------

        stack = []

        # Iterate through each asteroid in the input list
        for asteroid in asteroids:
            # Check for collisions while there are elements in the stack, the top of the stack is positive, and the current asteroid is negative
            while stack and stack[-1] > 0 and asteroid < 0:
                # Check for different collision scenarios
                if stack[-1] + asteroid < 0:
                    # If the sum is negative, pop the top asteroid from the stack
                    stack.pop()
                elif stack[-1] + asteroid == 0:
                    # If the sum is zero, both asteroids are destroyed, so pop the top asteroid and break out of the loop
                    stack.pop()
                    break
                else:
                    # If the sum is positive, break out of the loop
                    break
            else:
                # If there are no collisions, or the stack is empty, or the top of the stack is negative, push the current asteroid onto the stack
                stack.append(asteroid)

        # Return the stack containing surviving asteroids after collisions
        return stack
    
    