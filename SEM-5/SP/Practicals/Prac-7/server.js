var user = require('./user');
// var one = require('./1');
var category = require('./category');
var express = require('express');
var app = express();
app.use('/user',user);
app.use('/category',category);
// app.use('/1',one);
app.listen(3001);