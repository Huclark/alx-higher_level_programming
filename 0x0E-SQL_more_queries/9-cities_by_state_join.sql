-- Script that lists all cities contained in the database 'hbtn_0d_usa'
-- Each record displays;
-- 'cities.id' - 'cities.name' - 'states.name'
-- Results are displayed in ascending order by cities.id

-- Select the columns to retrieve data from
SELECT cities.id, cities.name, states.name
-- Select the table
FROM cities
-- Join the states table to the cities table
-- Otherwise states.name column will not be created
-- Since it is not an existing column under states
LEFT JOIN states ON states.id = cities.state_id
-- Order in ascending order by cities' id
ORDER BY cities.id ASC;
