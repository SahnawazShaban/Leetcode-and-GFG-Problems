"""
1174. Immediate Food Delivery II

Medium

Table: Delivery

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the column of unique values of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).
 

If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

The result format is in the following example.

 
Example 1:
Input: 
Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 2           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-12                  |
| 4           | 3           | 2019-08-24 | 2019-08-24                  |
| 5           | 3           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
| 7           | 4           | 2019-08-09 | 2019-08-09                  |
+-------------+-------------+------------+-----------------------------+
Output: 
+----------------------+
| immediate_percentage |
+----------------------+
| 50.00                |
+----------------------+
Explanation: 
The customer id 1 has a first order with delivery id 1 and it is scheduled.
The customer id 2 has a first order with delivery id 2 and it is immediate.
The customer id 3 has a first order with delivery id 5 and it is scheduled.
The customer id 4 has a first order with delivery id 7 and it is immediate.
Hence, half the customers have immediate first orders.

"""


# Solution 
# Write your MySQL query statement below

'''
SELECT ROUND(SUM(IF(order_date = customer_pref_delivery_date, 1, 0))*100/COUNT(DISTINCT customer_id), 2) AS immediate_percentage 
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM Delivery 
    GROUP BY customer_id
)

-- --------------------------------------------------------
-- Subquery:
-- SELECT customer_id, MIN(order_date) AS first_order_date
-- FROM Delivery 
-- GROUP BY customer_id

-- | customer_id | first_order_date |
-- | ----------- | ---------------- |
-- | 1           | 2019-08-01       |
-- | 2           | 2019-08-02       |
-- | 3           | 2019-08-21       |
-- | 4           | 2019-08-09       |
-- ---------------------------------------

-- select ROUND(AVG(order_date = customer_pref_delivery_date) * 100, 2) as immediate_percentage
-- from delivery where (customer_id, order_date) IN
-- (select customer_id, min(order_date) as first_order
-- from delivery
-- group by customer_id)

-- select round(sum(if(b.order_date = b.customer_pref_delivery_date, 1, null))/count(order_date)*100, 2) 
-- as immediate_percentage 
-- from ( select a.* from (select distinct * from Delivery order by order_date) a 
-- group by customer_id ) 




-- -- only store 1st order_date of each customer_id

-- +-------------+-------------+------------+-----------------------------+
-- | delivery_id | customer_id | order_date | customer_pref_delivery_date |
-- +-------------+-------------+------------+-----------------------------+
-- | 1           | 1           | 2019-08-01 | 2019-08-02                  |
-- | 2           | 2           | 2019-08-02 | 2019-08-02                  | 
-- | 3           | 1           | 2019-08-11 | 2019-08-12                  | - remove
-- | 4           | 3           | 2019-08-24 | 2019-08-24                  | - remove
-- | 5           | 3           | 2019-08-21 | 2019-08-22                  |
-- | 6           | 2           | 2019-08-11 | 2019-08-13                  | - remove
-- | 7           | 4           | 2019-08-09 | 2019-08-09                  |
-- +-------------+-------------+------------+-----------------------------+


-- +-------------+-------------+------------+-----------------------------+
-- | delivery_id | customer_id | order_date | customer_pref_delivery_date |
-- +-------------+-------------+------------+-----------------------------+
-- | 1           | 1           | 2019-08-01 | 2019-08-02                  | - S
-- | 2           | 2           | 2019-08-02 | 2019-08-02                  | - I
-- | 5           | 3           | 2019-08-21 | 2019-08-22                  | - S
-- | 7           | 4           | 2019-08-09 | 2019-08-09                  | - I
-- +-------------+-------------+------------+-----------------------------+

'''

# -NOTE- Whatever we use in 'GROUP BY' as we have written in 'SELECT'
