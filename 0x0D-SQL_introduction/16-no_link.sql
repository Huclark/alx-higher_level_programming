-- Script that lists all records of the table second_table of the
-- database hbtn_0c_0
-- Displays the score and the name columns, respectively.
-- Skips rows which does not have a name column value

-- Select the score and name columns
SELECT score, name
-- Specify table to retrieve data from
FROM second_table
-- Filter out rows without a name column value
WHERE name IS NOT NULL
-- Order by score column in a descending order
ORDER BY score DESC;
