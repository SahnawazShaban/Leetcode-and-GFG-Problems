/*
Score of two players after the alternative round of game

Given an array nums of size n. There are two people in the game P1 and P2, where P1 starts the game. The game is as follows:
Each person always chooses the first number in the nums adds it to their score and then removes the first element.
If the removed number is even then reverse the rest of the array. Print the final scores of p1 and p2.

Examples:
Input: nums = [1, 2, 4, 3]
Output: 4 6
Explanation: Turn1: Player1 pops 1 at index 0 and add it to their score score_p1 = 1 .Since it is odd we leave the array as it is so now the nums = [2,3,4] .Turn2: Player2 pops 2 at index 0, so score_p2 = 2,Since the popped number is even we reverse the array. So nums = [3,4] .Turn3: Player1 pops 3(odd) index so socre_p1 = 4; nums= [4]. Turn4: Player2 pops 4 at index 0 so score_p2 = 6. Popped number is even but nums =[] so we terminate and Output is: 4 6

Input: nums = {4, 3, 1, 2}
Output: 7 3
*/


//Solution

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // Example input
        List<Integer> nums = new ArrayList<>(Arrays.asList(4, 3, 1, 2));

        int[] scores = playGame(nums);

        // Output the final scores of Player 1 and Player 2
        System.out.println(scores[0] + " " + scores[1]);
    }

    public static int[] playGame(List<Integer> nums) {
        int score_p1 = 0;
        int score_p2 = 0;

        boolean isP1Turn = true;

        while (!nums.isEmpty()) {
            // Remove and get the first element from the list
            int num = nums.remove(0);

            // Add the number to the corresponding player's score
            if (isP1Turn) {
                score_p1 += num;
            } else {
                score_p2 += num;
            }

            // Check if the number is even, and if so, reverse the list
            if (num % 2 == 0 && !nums.isEmpty()) {
                Collections.reverse(nums);
            }

            // Switch turns
            isP1Turn = !isP1Turn;
        }

        return new int[]{score_p1, score_p2};
    }
}
