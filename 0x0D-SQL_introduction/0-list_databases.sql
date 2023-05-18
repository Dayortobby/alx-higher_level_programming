#!/bin/bash
-- lists all databases of your MySQL server.
# Prompt for MySQL root password
read -s -p "Enter MySQL root password: " mysql_password
echo

# Execute the SQL query to list databases
query="SHOW DATABASES;"
mysql -h localhost -u root -p"${mysql_password}" -e "${query}"
