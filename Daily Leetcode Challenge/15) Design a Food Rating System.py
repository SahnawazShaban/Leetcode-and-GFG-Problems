"""
2353. Design a Food Rating System

Medium

Design a food rating system that can do the following:

Modify the rating of a food item listed in the system.
Return the highest-rated food item for a type of cuisine in the system.
Implement the FoodRatings class:

FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
foods[i] is the name of the ith food,
cuisines[i] is the type of cuisine of the ith food, and
ratings[i] is the initial rating of the ith food.
void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.
Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

 
Example 1:
Input
["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
Output
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]

Explanation
FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
                                    // "kimchi" is the highest rated korean food with a rating of 9.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
                                      // "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // Both "sushi" and "ramen" have a rating of 16.
                                      // However, "ramen" is lexicographically smaller than "sushi".
 

Constraints:

1 <= n <= 2 * 10^4
n == foods.length == cuisines.length == ratings.length
1 <= foods[i].length, cuisines[i].length <= 10
foods[i], cuisines[i] consist of lowercase English letters.
1 <= ratings[i] <= 10^8
All the strings in foods are distinct.
food will be the name of a food item in the system across all calls to changeRating.
cuisine will be a type of cuisine of at least one food item in the system across all calls to highestRated.
At most 2 * 10^4 calls in total will be made to changeRating and highestRated.

"""


# Solution 

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.tracker = {}
        self.ratings = defaultdict(list)
        for f, c, r in zip(foods, cuisines, ratings): 
            self.tracker[f] = (c, r)
            heapq.heappush(self.ratings[c],[-r, f])

    def changeRating(self, food: str, newRating: int) -> None:
        c, r = self.tracker[food]
        heapq.heappush(self.ratings[c],[-newRating, food])
        # Update teh tracker
        self.tracker[food] = c, newRating
    

    def highestRated(self, cuisine: str) -> str:
        # remove all the redundant entries
        heap = self.ratings[cuisine]
        # now remove all the redundant
        while self.tracker[heap[0][1]][1] != -heap[0][0]:
            heapq.heappop(heap)

        return heap[0][1]

'''
import heapq
from collections import defaultdict
from typing import List

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # Dictionary to track cuisine and rating for each food
        self.tracker = {}
        # Dictionary to store a min heap of ratings for each cuisine
        self.ratings = defaultdict(list)
        
        # Initialize the tracker and ratings based on the provided data
        for food, cuisine, rating in zip(foods, cuisines, ratings): 
            self.tracker[food] = (cuisine, rating)
            # Use heapq to create a min heap for ratings with negative values
            heapq.heappush(self.ratings[cuisine], [-rating, food])

    def changeRating(self, food: str, newRating: int) -> None:
        # Retrieve cuisine and old rating for the given food
        cuisine, rating = self.tracker[food]
        
        # Push the new rating to the min heap
        heapq.heappush(self.ratings[cuisine], [-newRating, food])
        
        # Update the tracker with the new rating
        self.tracker[food] = cuisine, newRating

    def highestRated(self, cuisine: str) -> str:
        # Get the min heap for the specified cuisine
        heap = self.ratings[cuisine]
        
        # Remove redundant entries (entries with outdated ratings)
        while self.tracker[heap[0][1]][1] != -heap[0][0]:
            heapq.heappop(heap)
        
        # Return the food with the highest rating in the min heap
        return heap[0][1]

# Time Complexity:
# - Initialization: O(N * log(M)), where N is the number of foods and M is the average number of cuisines.
# - Change Rating: O(log(M)), where M is the average number of cuisines.
# - Highest Rated: O(log(M)), where M is the average number of cuisines.

# Space Complexity:
# - Tracker: O(N), where N is the number of foods.
# - Ratings: O(N * log(M)), where N is the number of foods and M is the average number of cuisines.

'''

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

