-- lists all cities of California found in database
SELECT id, name
FROM cities WHERE state_id in (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
