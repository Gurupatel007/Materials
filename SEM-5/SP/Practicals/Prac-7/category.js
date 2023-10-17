var express  = require('express');
var r = express.Router();
r.get('/display', (req, res)=>{
    res.send('category');
});
r.post('/add', (req, res)=>{
    res.send("post method for category");
});
r.put('/edit', (req, res)=>{
    res.send('put for category');
});
module.exports = r;