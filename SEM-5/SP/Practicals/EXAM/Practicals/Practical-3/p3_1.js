const http = require('http');
const url = require('url');

http.createServer((req,res)=>{
    if(req.url==='/'){
        res.write('Home page')
    }
    else if(req.url==='/exam'){
        res.write(`<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Timetable</title>
</head>
<body>
    <table border="solid">
        <tr>
            <th>Date</th>
            <th>Code</th>
            <th>Subject</th>
        </tr>
        <tr>
            <td>28/08/2023</td>
            <td>2CEIT501</td>
            <td>Computer Architecture and Organization</td>
        </tr>
        <tr>
            <td>30/08/2023</td>
            <td>2CEIT503</td>
            <td>Computer Network</td>
        </tr>
        <tr>
            <td>01/09/2023</td>
            <td>2CEIT5PE4</td>
            <td>Software Packages</td>
        </tr>
    </table>
</body>
</html>`)
    }
    else if(req.url==='/exam/semester_end'){
        res.writeHead(301,{'location':"https://sites.google.com/ganpatuniversity.ac.in/oddsem2023/5sem"})
    }
}).listen(1074,()=>{
    console.log('running at port 1074')
});