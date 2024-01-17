-- Script that lists all the cities of California that can be found in the database 'hbtn_0d_usa'

-- Select id and name columns
SELECT id, name
-- Select cities table
FROM cities
-- Create a subquery to pick only ids of cities from carlifonia 
WHERE state_id = (SELECT id FROM states WHERE name = 'california')
-- Prder the result in Ascending order
ORDER BY id ASC;
