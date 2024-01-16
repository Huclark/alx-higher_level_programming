-- Script that removes all records with a score <= 5 in the table second_table
-- of the database hbtn_0c_0

-- Select table to delete from
DELETE FROM second_table
-- Define criteria for deleting records
WHERE score <= 5;
