"""
1193. Monthly Transactions I

Medium

Table: Transactions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].
 

Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:
Input: 

Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+
Output: 
+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+

"""


# Solution 
# Write your MySQL query statement below

'''
-- SELECT DATE_FORMAT(trans_date, '%Y-%M') AS month, 
--        country, 
--        COUNT(id) AS trans_count,
--        SUM(IF(state = 'approved', 1, 0)) AS approved_count,
--        SUM(amount) AS trans_total_amount, 
--        SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount 
-- FROM Transactions 
-- GROUP BY month, trans_date 

-- | month         | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
-- | ------------- | ------- | ----------- | -------------- | ------------------ | --------------------- |
-- | 2018-December | US      | 1           | 1              | 1000               | 1000                  |
-- | 2018-December | US      | 1           | 0              | 2000               | 0                     |
-- | 2019-January  | US      | 1           | 1              | 2000               | 2000                  |
-- | 2019-January  | DE      | 1           | 1              | 2000               | 2000                  |

# SOLUTION - 1
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, 
       country, 
       COUNT(id) AS trans_count,
       SUM(IF(state = 'approved', 1, 0)) AS approved_count,
       SUM(amount) AS trans_total_amount, 
       SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount 
FROM Transactions 
GROUP BY month, country 


# SOLUTION - 2
SELECT  SUBSTR(trans_date,1,7) as month, 
        country, 
        count(id) as trans_count, 
        SUM(CASE WHEN state = 'approved' then 1 else 0 END) as approved_count, 
        SUM(amount) as trans_total_amount, 
        SUM(CASE WHEN state = 'approved' then amount else 0 END) as approved_total_amount
FROM Transactions
GROUP BY month, country


^^^^^^^^^^^
EXTRA WORK:
^^^^^^^^^^^
*****
EXAMPLES:

SELECT DATE_FORMAT(BirthDate, "%W %M %e %Y") FROM Employees;
OUTPUT:
Sunday December 8 1968
Tuesday February 19 1952

-----------------

DATEDIFF("2017-06-25", "2017-06-15")
10

------------------

SELECT OrderID, Quantity,
        CASE WHEN Quantity > 30 THEN 'The quantity is greater than 30'
        WHEN Quantity = 30 THEN 'The quantity is 30'
        ELSE 'The quantity is under 30'
        END AS QuantityText
FROM OrderDetails;

OrderID	  Quantity	QuantityText
10248	    12	    The quantity is under 30
10249	    40	    The quantity is greater than 30
10250	    10	    The quantity is under 30
10250	    35	    The quantity is greater than 30


IF(500<1000, "YES", "NO")
YES

IFNULL(expression, alt_value)
SELECT IFNULL(NULL, 500);
500

SELECT IFNULL("Hello", "sahnawazshaban.com");
Hello

SELECT IFNULL(NULL, "sahnawazshaban.com");
sahnawazshaban.com


SELECT SUBSTR("SQL Tutorial", 5, 3) AS ExtractString;
Tut
*****

'''

# -NOTE- Whatever we use in 'GROUP BY' as we have written in 'SELECT'
