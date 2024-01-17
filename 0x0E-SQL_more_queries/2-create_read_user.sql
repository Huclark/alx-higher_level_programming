-- Script that creates the database hbtn_0d_2 and the user 

-- Create database if does not exist
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';
-- Create a user if it does not exist and set its password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant select permission to user.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
