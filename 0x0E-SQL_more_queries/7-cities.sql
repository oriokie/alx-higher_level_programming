-- Creates the database hbtn_0d_usa with the table cities.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Use the hbtn_0d_usa database
USE `hbtn_0d_usa`;
-- Create the cities table if it does not exist
CREATE TABLE IF NOT EXISTS `cities` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `state_id` INT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`state_id`) REFERENCES `states`(`id`)
	);
