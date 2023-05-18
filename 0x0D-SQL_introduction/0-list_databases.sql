#!/bin/bash
-- Execute the SQL query to list databases
query="SHOW DATABASES;"
mysql -h localhost -u root -p"${mysql_password}" -e "${query}"
