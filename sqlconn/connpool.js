var express = require("express");
var mysql = require("mysql");

var pool = mysql.createPool({
    connectionLimit : 100,
    host : '172.17.0.2',
    user : 'root',
    password : 'running',
    database : 'mysql',
    debug : false
});
var app = express()


function handle_database(req,res) {
  // connection will be acquired automatically
  pool.query("select * from user",function(err,rows){
   if(err) {
       return res.json({'error': true, 'message': 'Error occurred'+err});
   }
           //connection will be released as well.
           res.json(rows);
  });
}

}
app.get("/",function(req,res){-
  handle_database(req,res);
});

app.listen(4000);
