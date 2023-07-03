-- https://stackoverflow.com/questions/17250243/how-to-return-null-when-result-is-empty
-- How to return NULL when result is empty
select
  (Your entire current Select statement goes here) as Alias

# sex column 的 m,f 交換
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
