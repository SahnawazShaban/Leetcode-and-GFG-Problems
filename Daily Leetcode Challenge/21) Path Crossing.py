"""
1496. Path Crossing

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.


Example 1:

Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:

Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
 

Constraints:

1 <= path.length <= 10^4
path[i] is either 'N', 'S', 'E', or 'W'.

"""


# Solution 

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Dictionary to map each direction to its corresponding change in coordinates
        direction_axis = {
            'E': (1, 0),
            'W': (-1, 0),
            'N': (0, 1),
            'S': (0, -1)
        }

        # Set to store visited coordinates, starting with the initial position (0, 0)
        visited = {(0, 0)}
        x = y = 0  # Initial position

        # Iterate through each direction in the path
        for i in path:
            # Get the change in coordinates for the current direction
            dx, dy = direction_axis[i]

            # Update the current position
            x += dx
            y += dy

            # Check if the new position has been visited before
            if (x, y) in visited:
                return True  # Path crosses itself

            # Add the new position to the set of visited coordinates
            visited.add((x, y))

        # If the loop completes without returning True, the path does not cross itself
        return False

'''
Time Complexity:
The time complexity of the code is O(N), where N is the length of the input path string. The function iterates through each character in the path exactly once, performing constant-time operations for each step. The primary operation within the loop involves updating the current position, checking if the position has been visited, and adding the position to the set of visited coordinates—all of which are constant time. Therefore, the time complexity is linear with respect to the length of the input path.

Space Complexity:
The space complexity of the code is also O(N), where N is the length of the input path string. The dominant factor contributing to space complexity is the set visited, which stores the unique coordinates visited by the wanderer. In the worst case, the set could contain all unique coordinates visited during the entire path, and therefore, its size is directly proportional to the length of the path. Other variables like x and y and the direction_axis dictionary require constant space.
'''

