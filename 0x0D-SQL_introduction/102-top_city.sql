-- Script that displays the top 3 of cities temperature during
-- July and August ordered by temperature in descending order

-- Select the city column
SELECT city,
-- Calculate the average temperature in value column
AVG(value)
-- Put the averages in the avg_temp column
AS avg_temp
-- Import the temperatures file
FROM temperatures
-- Filter results to include only data for only July or August in the month column
WHERE month = 7 or month = 8
-- Group results by the city column
GROUP BY city
-- Order results in the avg_temp in descending order
ORDER BY avg_temp DESC
-- Limit the results to the top 3 cities
LIMIT 3;
