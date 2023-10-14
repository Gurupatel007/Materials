`Create a Node.js program that serves an HTML page with a form to collect user input for book
details. The form should collect information such as Book Title, Author and Price. When the form is
submitted, the program should store the collected data into a file named book_data.txt.`
// Code:
// // app.js
const http = require('http');
const fs = require('fs');
const server = http.createServer(function (req, res) {
    if (req.url === '/') {
        fs.readFile('./index.html', function (err, data) {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.write(data);
            res.end();
        });
    }
    else if (req.url === '/submit') {
        let body = '';
        req.on('data', function (chunk) {
            body += chunk;
        });
        req.on('end', function () {
            let obj = JSON.parse(body);
            let book = {
                Title: obj.title,
                author: obj.author,
                price: obj.price
            };
            fs.appendFile('book_data.txt', JSON.stringify(book) + '\n', function (err) {
                if (err) throw err;
                console.log('Saved!');
            });
            res.end();
        });
    }
});
server.listen(3000);
console.log('Server started on port 3000');
