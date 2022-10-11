-- Setup for Primary MySQL server to replicate from

-- Create a database name: tyrell_corp
CREATE DATABASE IF NOT EXISTS tyrell_corp;

-- Create a table (name nexus6) on tyrell_corp
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
	id INT NOT NULL AUTO_INCREMENT UNIQUE,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
);

-- Insert a new row in the table nexus6
INSERT INTO nexus6 (name) VALUES('Leon');

-- Grant Select permission to holberton_user
GRANT SELECT ON tyrell_corp.* TO 'holberton_user'@'localhost';
