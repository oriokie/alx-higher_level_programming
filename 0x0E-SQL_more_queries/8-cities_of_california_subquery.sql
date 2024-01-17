-- lists all the cities of California in the database
SELECT * FROM `cities`
WHERE `state_id` IN (
	SELECT `id` FROM `states`
    WHERE `name` = "California")
ORDER BY `id` ASC;
