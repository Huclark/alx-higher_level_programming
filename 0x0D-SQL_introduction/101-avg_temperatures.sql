-- Script that displays the average temperature(Farenheit) by city
-- ordered by temperature (Descending order)

-- Select the city column
SELECT city,
-- Use AVG() to calulate the average of score of the value column
AVG(value)
-- Assign the result to the avg_temp column
AS avg_temp
-- Specify path to the temperatures file
FROM temperatures
-- Group the results by the 'city' COLUMN
GROUP BY city
-- Order the results in descending order based on the average temperature
ORDER BY avg_temp DESC;
