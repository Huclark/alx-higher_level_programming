-- Script that creates a table 'second_table' in the database 'hbtn_0c_0'
-- and add multiple rows

-- Create table with description
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
-- Insert new row into the table
INSERT INTO second_table(id, name, score)
-- Specify the values of each column
VALUES (1, "John", 10);
-- Insert new row into the table
INSERT INTO second_table(id, name, score)
-- Specify the values of each column
VALUES (2, "Alex", 3);
-- Insert new row into the table
INSERT INTO second_table(id, name, score)
-- Specify the values of each column
VALUES (3, "Bob", 14);
-- Insert new row into the table
INSERT INTO second_table(id, name, score)
-- Specify the values of each column
VALUES (4, "George", 8);
