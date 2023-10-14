const http = require('http');
const url = require('url');
http.createServer((req, res) => {
    const u = url.parse(req.url, true)
    console.log(u)
    var n1 = parseInt(u.query.num1); 
    var n2 = parseInt(u.query.num2);
    var number1 = n1.toString();
    var number2 = n2.toString();
    n1 > n2 ? res.write(number1) : res.write(number2)

    res.end()
}).listen(5000,()=> console.log('server is running'));