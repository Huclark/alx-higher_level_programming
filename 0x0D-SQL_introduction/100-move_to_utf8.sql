-- Script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- Converts all of the following to UTF8;
-- Database hbtn_0c_0
-- Table first_table
-- Field name in first_table

-- Switch to the 'hbtn_0c_0' database
USE `hbtn_0c_0`
-- Begin ALTERTABLE statement to modify the 'first_table' table
-- Specify the new character set for the table as utf8mb4
-- Specify the new collation for the table as 'utf8mb4_unicode_ci'
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
