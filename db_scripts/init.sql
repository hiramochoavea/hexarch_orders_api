-- Create the database
CREATE DATABASE IF NOT EXISTS orders_db;

-- Grant permissions to the user
GRANT ALL PRIVILEGES ON *.* TO 'orders_user'@'%' WITH GRANT OPTION;

-- Flush privileges to ensure they take effect
FLUSH PRIVILEGES;