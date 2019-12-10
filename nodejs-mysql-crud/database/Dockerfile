
##Create data folder ${PWD}/dbdata,  ${PWD}/dbdump, Restore the data here

FROM mysql:5.6

ARG MYSQL_PASSWORD=
ARG MYSQL_ROOT_PASSWORD=

ENV MYSQL_PASSWORD=$MYSQL_PASSWORD
ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD

EXPOSE 3306
EXPOSE 33060

ADD init_db.sh /tmp/init_db.sh
RUN /tmp/init_db.sh


#!/bin/bash
/usr/bin/mysqld_safe --skip-grant-tables &
sleep 5
mysql -u root -e "CREATE DATABASE mydb"
mysql -u root mydb < /tmp/dump.sql







