// https://codeforgeek.com/nodejs-mysql-tutorial/#code-for-production-

var express = require("express");
var mysql = require("mysql");

var connection = mysql.createConnection({
    host : '172.17.0.2',
    user : 'root',
    password : 'running',
    database : 'mysql'  
});
var app = express()

conn.connect(function(err){
    if(!err) {
        console.log("Database connection is success");
    }
    else {
        console.log("Error connection .... ");
    }
});

app.get("/",function(req,res){
    connection.query('SELECT * from user LIMIT 2', function(err, rows, fields) {
    connection.end();
      if (!err)
        console.log('The solution is: ', rows);
      else
        console.log('Error while performing Query.');
      });
    });

app.listen(3000);
