"""
621. Task Scheduler

Medium

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.


Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

Constraints:

1 <= task.length <= 10^4
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].

"""

# SOLUTION

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Create a dictionary to store the frequency of each task
        temp_dict = {}

        # Count the occurrences of each task and store in the dictionary
        for alpha in tasks:
            temp_dict[alpha] = temp_dict.get(alpha, 0) + 1

        # Sort the values (task frequencies) in descending order
        lst = sorted(temp_dict.values(), reverse=True)

        # The maximum frequency of a task
        max_ele = lst[0]

        i = 0
        count = 0

        # Count the number of tasks with the maximum frequency
        while i < len(lst) and lst[i] == max_ele:
            i += 1
            count += 1

        # Calculate the total time required based on the given formula
        res = (max_ele - 1) * (n + 1) + count

        # Return the maximum of the calculated time and the total number of tasks
        return max(res, len(tasks))

'''
Time Complexity:
The loop that iterates through the tasks to build the frequency dictionary has a time complexity of O(N), where N is the number of tasks.
Sorting the values of the dictionary has a time complexity of O(K log K), where K is the number of unique tasks.
The while loop that counts the number of tasks with the maximum frequency also has a time complexity of O(K), where K is the number of unique tasks.
The overall time complexity is dominated by the sorting step, so it can be expressed as O(N + K log K).


Space Complexity:
The space complexity is primarily determined by the temp_dict dictionary, which stores the frequency of each task. In the worst case, where all tasks are unique, the space complexity is O(N).
The lst list also contributes to the space complexity, and in the worst case, it can be O(K), where K is the number of unique tasks.
Other variables used in the function have constant space requirements.
'''
