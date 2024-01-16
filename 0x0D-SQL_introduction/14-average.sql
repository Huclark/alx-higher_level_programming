-- Script that computes the score average of all records in the table second_table
-- of the database hbtn_0c_0

-- Use AVG() to calulate the average of score
SELECT AVG(score)
-- Assign it to a new column
AS average
-- specify the table to update
FROM second_table;
