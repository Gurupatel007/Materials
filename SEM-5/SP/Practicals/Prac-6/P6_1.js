const { query } = require('express');
var m=require('mysql')

var conn=m.createConnection({
    'host':'localhost',
    'user':'root',
    'password':'',
    'port':'3307'
});

conn.connect((err) => {
  if (err) {
    console.error('Error connecting to MySQL database:', err);
  } else {
        console.log('Connected to MySQL database');

        var x='create database Node_test';
        
        conn.query(x,(err) => {
                if (err) {
                console.error('Error creating database:', err);
                } else {
                console.log('Database created successfully');
                }
                conn.end();
        });
    }
});