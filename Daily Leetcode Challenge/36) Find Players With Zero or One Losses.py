"""
2225. Find Players With Zero or One Losses

Medium

You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
 

Example 1:
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

Example 2:
Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
 

Constraints:

1 <= matches.length <= 10^5
matches[i].length == 2
1 <= winneri, loseri <= 10^5
winneri != loseri
All matches[i] are unique.

"""


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Brute Force
        '''
        winner = []
        loser = []

        for i in range(len(matches)):
            winner.append(matches[i][0])
            loser.append(matches[i][1])

        temp_dict = {}

        for val in loser:
            temp_dict[val] = temp_dict.get(val, 0) + 1

        winner = set(winner)
        loser = set(loser)

        new_winner = list(winner)
        for w in winner:
            if w in loser:
                new_winner.remove(w)


        new_loser = []
        for key, val in temp_dict.items():
            if val == 1:
                new_loser.append(key)

        
        return [sorted(new_winner), sorted(new_loser)]
        '''

        # ---------------------------------

        # Optimal
        temp_dict = {}
        for val in matches:
            temp_dict[val[1]] = temp_dict.get(val[1], 0) + 1

        win, loss=set(),[]
        for pair in matches:
            if pair[0] not in temp_dict:
                win.add(pair[0])

        for key, val in temp_dict.items():
            if val == 1:
                loss.append(key)

        win = list(win)
        win.sort()
        loss.sort()
        return [win, loss]


'''
Brute Force Approach:

Time Complexity:
The loop to extract winners and losers has a time complexity of O(N), where N is the number of matches.
The loop to count losses and filter winners also has a time complexity of O(N).
Sorting the lists has a time complexity of O(N log N).
Therefore, the overall time complexity is O(N log N).

Space Complexity:
The space complexity is O(N) due to the use of sets and lists to store winners, losers, and the temporary dictionary.


Optimal Approach:

Time Complexity:
The loop to count losses has a time complexity of O(N), where N is the number of matches.
The loop to filter winners has a time complexity of O(N).
Sorting the lists has a time complexity of O(N log N).
Therefore, the overall time complexity is O(N log N).

Space Complexity:
The space complexity is O(N) due to the use of sets and lists to store winners and the temporary dictionary.
Both approaches have the same time and space complexity, but the optimal approach simplifies the code and avoids unnecessary steps, making it more concise and efficient.
'''
