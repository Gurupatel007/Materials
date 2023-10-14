const http = require('http');
const url = require('url');
const mysql = require('mysql');

// create connection to mysql database
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    port : "3307",
    database: 'Node_test'
});

// connect to mysql database
connection.connect((err) => {
    if (err) throw err;
    console.log('Connected to MySQL database!');
});

// create http server
http.createServer((req, res) => {
    // parse url
    const q = url.parse(req.url, true);
    // check if request is for form submission
    if (q.pathname === '/submit') {
        // get product information from form data
        const string = q.query;
        const name = string.name;
        const brand = string.brand;
        const quantity = string.quantity;
        const price = string.price;
        // insert product into mysql database
        const query = "insert into product(name, brand, quantity, price) values('" + name + "', '" + brand + "', '" + quantity + "', '" + price +"')";
        connection.query(query , (err, result) => {
            if (err) throw err;
            console.log('Product inserted into MySQL database!');
            // send response to client
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write('<h1>Product inserted into MySQL database!</h1>');
            res.end();
        });
    } else {
        // send html form to client
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write('<form action="/submit" method="get">');
        res.write('<label for="name">Name:</label>');
        res.write('<input type="text" id="name" name="name"><br><br>');
        res.write('<label for="brand">Brand:</label>');
        res.write('<input type="text" id="brand" name="brand"><br><br>');
        res.write('<label for="quantity">Quantity:</label>');
        res.write('<input type="number" id="quantity" name="quantity"><br><br>');
        res.write('<label for="price">Price:</label>');
        res.write('<input type="number" id="price" name="price"><br><br>');
        res.write('<input type="submit" value="Submit">');
        res.write('</form>');
        res.end();
    }
}).listen(5050, () => {
    console.log('Server listening on port 8080!');
});
