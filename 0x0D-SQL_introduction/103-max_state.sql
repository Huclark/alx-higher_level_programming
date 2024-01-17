-- Script that displays the max temperature of each state (ordered by State name)

-- Select the state column
SELECT state,
-- Ascertain the max temperature in the value column
MAX(value)
-- Assign the results to the max_temp column
AS max_temp
-- Import the temperatures file
FROM temperatures
-- Group results by state column
GROUP BY state
-- Order by max_temp column in descending order
ORDER BY max_temp DESC;
