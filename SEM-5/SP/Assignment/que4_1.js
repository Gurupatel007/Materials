var http = require('http');
var fs = require('fs');
var qs = require('querystring');

http.createServer((req,res) =>
{
    if(req.method == 'POST')
    {
        var data = '';
        req.on('data',(c)=>
        {
            data = data + c;
        });
    
        req.on('end',()=>
        {
           var formData = qs.parse(data.toString());
           var bookDetails = `Book Title: ${formData.title}
           \nBook Author: ${formData.author}
           \nBook Price: ${formData.price}\n\n`;
           fs.writeFile('book_data.txt', bookDetails, (err) => {
            if (err) {
                res.write(err.message);
                res.end();
            } 
            else 
            {
                res.write(`<h1>Book Details Saved:</h1><p>${bookDetails}</p>`);
                res.end();
            }
            });
        });
    }

    else 
    {
        fs.readFile('E:/SEMwise Materials/SEM-5/SP/Assignment/index.html',(err,code)=>
        {
            if (err) {
                res.write(err.message);
                res.end();
            }
            else
            {
                res.writeHead(200,{'content-type':'text/html'});
                res.write(code);
                res.end();
            }
        });
    }

}).listen(1072);