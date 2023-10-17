var express  = require('express');
var r = express.Router();
r.get('/display', (req, res)=>{
    res.send('user');
});
r.post('/add', (req, res)=>{
    res.send("post method for user");
});
r.put('/edit', (req, res)=>{
    res.send('put for user');
});
module.exports = r;