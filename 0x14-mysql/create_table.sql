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

-- Create a new user with following credential:
-- username => replica_user
-- hostname => %
-- password => password
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'password';

-- Grant appropriate permissions to replica_user
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- Grant Select permission to holberton_user ON all tables of tyrell_corp
GRANT SELECT ON tyrell_corp.* TO 'holberton_user'@'localhost';

-- Grant SELECT permission to holberton_user ON user table of mysql database
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
