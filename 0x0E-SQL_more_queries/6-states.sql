-- Script that creates the database 'hbtn_0d_usa' and the table 'states'
-- in the hbtn_0d_usa database with the description;
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can't be null

-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table if it does not exist and populate it
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
