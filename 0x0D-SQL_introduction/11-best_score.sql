-- Script that lists all records with a score >= 10
-- in the second_table of the database'hbtn_0c_0'
-- Displays both the score and the name, respectively.
-- Records are ordered by score (top first)

-- Select the columns to display
SELECT score, name
-- Select the table to retrieve data from
FROM second_table
-- Filter out results to get rows with scores >= 10
WHERE score >= 10
-- Order the results in descending order on the 'score' column
ORDER BY score DESC;
