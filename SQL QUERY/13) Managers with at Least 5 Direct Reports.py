"""
570. Managers with at Least 5 Direct Reports

Medium

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
 

Write a solution to find managers with at least five direct reports.

Return the result table in any order.

The result format is in the following example.

 
Example 1:
Input: 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output: 
+------+
| name |
+------+
| John |
+------+

"""


# Solution 
# Write your MySQL query statement below

'''
-- SELECT *
-- FROM Employee e1
-- INNER JOIN Employee e2
-- ON e1.id = e2.managerId

-- answer
-- | id  | name | department | managerId | id  | name  | department | managerId |
-- | --- | ---- | ---------- | --------- | --- | ----- | ---------- | --------- |
-- | 101 | John | A          | null      | 102 | Dan   | A          | 101       |
-- | 101 | John | A          | null      | 103 | James | A          | 101       |
-- | 101 | John | A          | null      | 104 | Amy   | A          | 101       |
-- | 101 | John | A          | null      | 105 | Anne  | A          | 101       |
-- | 101 | John | A          | null      | 106 | Ron   | B          | 101       |


-SOLUTION-

SELECT e1.name
FROM Employee e1
INNER JOIN Employee e2
ON e1.id = e2.managerId
GROUP BY e2.managerId
HAVING COUNT(e2.managerId) >= 5

'''

# -NOTE- Whatever we use in 'GROUP BY' as we have written in 'SELECT'
