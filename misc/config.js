/* File: config.js */
// for MVC by nodejs-express-mysql from git
module.exports = {
    app : {
        name: 'node-mysql',
        protocol: 'http',
        port: 8080,
        version: '1.0.0'
    },
    mysql: {
        host: '172.17.0.2',
        port: 3306,
        user: 'root',
        password: 'running',
        database: 'Server'
    },
    morgan: {
        mode: 'dev'
    }
};