#!/bin/sh

echo "Get the dump file"
sleep 15
echo "Start the docker with volumnes ./dbdata "
docker exec -i ${mm} sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < dbdump/all-databases.sql