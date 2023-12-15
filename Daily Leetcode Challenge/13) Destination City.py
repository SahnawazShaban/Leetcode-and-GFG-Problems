"""
1436. Destination City

Easy

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.


Example 1:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

Example 3:
Input: paths = [["A","Z"]]
Output: "Z"
 

Constraints:

1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAi.length, cityBi.length <= 10
cityAi != cityBi
All strings consist of lowercase and uppercase English letters and the space character.

"""


# Solution 

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Solution - 1
        # collecting the departure cities
        departure = set()
        for cities in paths:
            departure.add(cities[0])

        # if we encounter city that is not in the departure list, then it should be the desitnation
        for cities in paths:
            if cities[1] in departure:
                continue
            else:
                return cities[1]

        # -----------------------------------------

        # Solution - 2
        '''
        source = set()
        dest = set()
        
        # Iterate through each path in the list of paths
        for l in paths:
            # Add the source city to the 'source' set
            source.add(l[0])
            
            # Add the destination city to the 'dest' set
            dest.add(l[1])
        
        # Return the first (and only) element in the set difference between 'dest' and 'source'
        return list(dest - source)[0]
        '''