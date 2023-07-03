-- https://stackoverflow.com/questions/17250243/how-to-return-null-when-result-is-empty
-- How to return NULL when result is empty
select
  (Your entire current Select statement goes here) as Alias

-- sex column 的 m,f 交換
Salary table:
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
+----+------+-----+--------+

UPDATE salary SET sex =
CASE sex
    WHEN 'm' THEN 'f'
    ELSE 'm'
END;

-- 在 SQL 的 GROUP BY 子句中，可以使用聚合函數（Aggregate Function）來對分組的數據進行計算，包括 SUM、AVG、COUNT、MIN、MAX 等。如果需要在 GROUP BY 子句中進行相減的操作

SELECT user_id, MAX(price) - MIN(price) as diff
FROM orders
GROUP BY user_id;

-- JOIN = INNER JOIN

-- PIVOT
-- salesperson  sale_date  amount
-- --------------------------------
-- Alice        2022-01-01  100
-- Bob          2022-01-01  200
-- Charlie      2022-01-01  150
-- Alice        2022-01-02  120
-- Bob          2022-01-02  220
-- Charlie      2022-01-02  180

SELECT *
FROM sales
PIVOT (
  SUM(amount)
  FOR sale_date IN ('2022-01-01', '2022-01-02')
) AS p;

-- salesperson  2022-01-01  2022-01-02
-- -------------------------------------
-- Alice         100         120
-- Bob           200         220
-- Charlie       150         180

-- UNPIVOT
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+

SELECT product_id,store,price
FROM Products
UNPIVOT
(
	price
	FOR store in (store1,store2,store3)
) AS T

+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store3 | 80    |
+------------+--------+-------+

-- 創建一個欄位，全都同一個數值 (會創一個 status 的欄位，裡面全都是 "NEW")
SELECT order_id, customer_id, order_date, 'NEW' AS status
FROM orders;
