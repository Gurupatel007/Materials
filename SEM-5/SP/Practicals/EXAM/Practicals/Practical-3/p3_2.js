const http = require('http')
const url = require('url');

http.createServer((req,res)=>{
    const q = url.parse(req.url,true)
    console.log(q);
    var n1 = parseInt(q.query.num1);
    var n2 = parseInt(q.query.num2);
    var num1 = n1.toString();
    var num2 = n2.toString();
    n1>n2 ?res.write(num1):res.write(num2);
    
    res.end()
}).listen(1074,()=> console.log('running on 1074'));