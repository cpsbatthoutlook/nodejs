

##Create data folder ${PWD}/dbdata,  ${PWD}/dbdump, Restore the data here
PWD=<<mention the folder>>
mkdir -p ${PWD}/dbdata  ${PWD}/dbdump
cd ${PWD} 
Copy Dockerfile here
Get the file from mysqldump folder

# m5=mysql:5.6
# mm=mysql
# mysqlimage=$m5
# vv=/var/lib/mysql
# lv=${pwd}/dbdata
# docker run --name $mm  -p 3306:3306 -p 33060:33060  -e MYSQL_ROOT_HOST='%' -e MYSQL_ROOT_PASSWORD='strongpassword' -d ${mysqlimage}
# docker run --name $mm  -p 3306:3306 -p 33060:33060 -v ${PWD}/dbdata:${vv}   -e ^CSQL_ROOT_PASSWORD=running -d ${mysqlimage}

#  docker run -it --rm ${m5} mysql -h172.17.0.2 -uroot -p

## Mysql available options
# docker run -it --rm mysql:tag --verbose --help 


#With External volumes
# docker run --name some-mysql -v ${pwd}/datadir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d ${mysqlimage}

##Custom Configs
# docker run --name mysql -v /my/custom:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=my-secret-pw -d ${mysqlimage}

##Dump all databases
#  docker exec mysql5 sh -c 'exec mysqldump --all-databases -uroot -p"$MYSQL_ROOT_PASSWORD"' > dbdump/all-databases.sql
##Dump all restore
# docker exec -i ${mm} sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < dbdump/all-databases.sql