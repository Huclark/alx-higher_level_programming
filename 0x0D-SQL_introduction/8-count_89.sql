-- Script to display the number of records with "id = 89" in the "first_table"
-- of the database "htbn_0c_0"

-- Selecting the count of rows
SELECT COUNT(*)
-- Specify the table
FROM first_table
-- Filter out rows where the id value is 89
WHERE id = 89
