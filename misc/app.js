var express         = require('express'),
    session             = require('express-session'),
    bodyParser      = require('body-parser'),
    compression     = require('compression'),
    cookieParser    = require('cookie-parser'),
    flash           = require('connect-flash'),
    morgan          = require('morgan'),
    mysql           = require('mysql'),
    passport        = require('passport'),
    // Main Application Object
    app             = express(),
    // Passport Strategy
    BearerStrategy      = require('passport-http-bearer').Strategy,
    LocalStrategy       = require('passport-local').Strategy,
    // 
    config                      = require('./config');

// https://github.com/imamhidayat92/nodejs-express-mysql.git

console.log();
console.log('Script executed at ' + (new Date()));
console.log();

/* Initialize connection to MySQL */
var connector = mysql.createConnection(config.mysql);
connector.connect(function(err) {
    if (err) {
        console.error('Error while connecting to MySQL: ' + err.stack);
        return;
    }
    console.log(config.app.name + ' has been connected to MySQL successfully.');
});

