-- Script that lists all records of the table 'second_table' of the 'htbn_0c_0' database
-- Displays both the score and the name, respectively.
-- Records are ordered by score (top first).

-- Select the values to display
SELECT score, name
-- Select the table to retrieve data from
FROM second_table
-- Order the results in descending order on the 'score' column
ORDER BY score DESC;
