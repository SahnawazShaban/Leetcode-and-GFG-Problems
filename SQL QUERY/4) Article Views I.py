"""
1148. Article Views I
Solved
Easy
Topics
Companies
SQL Schema
Pandas Schema
Table: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.
 

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

The result format is in the following example.

 

Example 1:

Input: 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output: 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+

"""


# Solution 
# Write your MySQL query statement below

'''
SELECT DISTINCT author_id as id 
FROM Views
WHERE author_id = viewer_id 
ORDER BY id ASC
'''

# referee_id = NULL : this is not working
# The 'not equal' operator in MySQL is represented by <> or !=.

# ASC - Ascending 
# DESC - Descending 


'''
In SQL, the AS keyword is used to alias a column or a table. 
An alias is a temporary name that you can assign to a column or a table in the result set of a query. 
It is often used for readability and to provide a more meaningful name to a column or table.


Example

SELECT column_name AS alias_name
FROM table_name;

SELECT t1.column_name, t2.column_name
FROM table1 AS t1
INNER JOIN table2 AS t2 ON t1.id = t2.id;
'''
