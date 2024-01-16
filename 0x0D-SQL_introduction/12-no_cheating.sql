-- Script that updates the score of Bob to 10 in the table 'second_table'
-- Using only the name field

-- Specify the table to update
UPDATE second_table
-- Update the score value
SET score = 10
-- Specify the name to UPDATE
WHERE name = 'Bob';
