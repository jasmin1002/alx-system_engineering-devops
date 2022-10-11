-- Create a database user with following credentials:
-- username: holberton_user
-- password: projectcorrection280hbtn
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

-- Grant permission for holberton_user
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
