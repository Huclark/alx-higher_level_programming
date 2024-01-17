-- Script that creates the table id_not_null with the description;
-- id INT with the default value 1
-- name VARCHAR(256)

-- Create table if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 0,
	name VARCHAR(256)
)
