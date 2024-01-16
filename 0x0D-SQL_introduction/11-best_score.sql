-- select all the records
-- where the score is eq or more than 10
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
