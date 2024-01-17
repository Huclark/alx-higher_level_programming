-- Script that lists the number of records with the same score
-- in the table second_table of the database hbtn_0c_0

-- Select the score column
SELECT score
-- Count number of occurences of each score and assign value to number column
COUNT(*) as number
-- Specify the table from which to retrieve data
FROM second_table
-- Order the results in descending order
GROUP BY score ORDER BY number DESC;
