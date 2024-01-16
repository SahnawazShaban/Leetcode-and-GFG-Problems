"""
380. Insert Delete GetRandom O(1)

Medium

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.


Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.

"""


# SOLUTION

class RandomizedSet:

    def __init__(self):
        # Dictionary to store mapping of values to their indices in the list
        self.temp_dict = {}

        # List to store the actual values
        self.temp_list = []

    def insert(self, val: int) -> bool:
        # Check if the value is not already in the set
        res = val not in self.temp_dict

        if res:
            # If not present, add the value to the dictionary with its index in the list
            self.temp_dict[val] = len(self.temp_list)
            # Append the value to the list
            self.temp_list.append(val)

        return res

    def remove(self, val: int) -> bool:
        # Check if the value is present in the set
        res = val in self.temp_dict

        if res:
            # If present, get the index of the value in the list
            idx = self.temp_dict[val]
            # Get the last value in the list
            last_val = self.temp_list[-1]
            # Replace the value at index 'idx' with the last value
            self.temp_list[idx] = last_val
            # Update the mapping for the last value in the dictionary
            self.temp_dict[last_val] = idx
            # Remove the last value from the list
            self.temp_list.pop()
            # Delete the mapping for the removed value
            del self.temp_dict[val]

        return res

    def getRandom(self) -> int:
        # Return a random value from the list
        return random.choice(self.temp_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()