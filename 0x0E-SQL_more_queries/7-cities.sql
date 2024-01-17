-- Script that creates the database 'hbtn_0d_usa' and the table 'cities'
-- in the 'hbtn_0d_usa' database with the description;
-- id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
-- name VARCHAR(256) can’t be null

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table if it doesn't exist
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
	name VARCHAR(256) NOT NULL
);
