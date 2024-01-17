-- Script for creating the database hbtn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Use the new database created
USE `hbtn_0d_usa`;
-- create the states table
CREATE TABLE IF NOT EXISTS `states` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL,
	PRIMARY KEY(`id`)
	);
