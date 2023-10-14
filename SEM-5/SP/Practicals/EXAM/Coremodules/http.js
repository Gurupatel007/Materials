var http = require('http');
http.createServer((req,res)=>{
//    res.write("Hello it's g.t");
    res.writeHead(200,{'Content-Type':'text/html'});
    res.write(req.url);
    res.end();
}).listen(1074);
console.log("Running at port 1074");