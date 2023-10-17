var express  = require('express');
var parse = require('body-parser');
var app      = express();
app.use(parse.json());
var products = [
    {'pid': 1,'name':'p1','brand':'b1'},
    {'pid': 2,'name':'p2','brand':'b2'},
    {'pid': 3,'name':'p3','brand':'b3'}
];
app.get('/products', function(req, res) {
    res.json(products);
});
app.post('/products', function(req, res) {
    products.push(req.body);
    // res.json(products);
    res.send(req.body);
});
app.put('/products/:id', function(req, res) {
    // products[req.params.id] = req.body;
    // res.json(products);
    var id1 = req.params.id;
    var r  = req.body.name;
    products.map((ss)=>{
        if(ss.pid===Number(id1)){
            ss.name=r;
        }
    });
    res.send(products);
});
app.listen(3001);