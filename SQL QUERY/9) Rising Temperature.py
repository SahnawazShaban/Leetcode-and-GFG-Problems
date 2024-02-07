"""
197. Rising Temperature

Easy

Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.
 

Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The result format is in the following example.

 

Example 1:
Input: 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Output: 
+----+
| id |
+----+
| 2  |
| 4  |
+----+
Explanation: 
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).

"""


# Solution 
# Write your MySQL query statement below

'''
SELECT w1.id
FROM Weather w1
INNER JOIN Weather w2
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperature

# Instead of 'ON', we can use 'WHERE'

'''

# -------------------------------------------
# EXTRA

# After SELECT keyword column is same as after 'GROUP BY' column
# -NOTE- whenever we use 'Aggregate Functions' at that time, we can use 'group by'


'''
Aggregate Functions:
1. sum()
2. count()
3. min()
4. max()
5. avg()
'''
