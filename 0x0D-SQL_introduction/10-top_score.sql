-- Script that lists all records of the table 'second_table' of the 'htbn_0c_0' database
-- Displays both the score and the name, respectively.
-- Records are ordered by score (top first).

-- Select the values to display
SELECT score, name
-- Order the scores by highest score first
FROM second_table ORDER BY score DESC;
