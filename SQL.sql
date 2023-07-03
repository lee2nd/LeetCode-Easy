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
