// `Create a Node.js script that generates an HTML file (dynamic.html) dynamically. 
// The HTML file should contain a table with data from an array of objects. Each 
// object represents a person with properties like name, age, and city. Display the data 
// in the table and style it with CSS.`
// Path: p4_5.js
// // Define an array of objects
var people = [
  { name: 'John', age: 25, city: 'London' },
  { name: 'Jane', age: 20, city: 'New York' },
  { name: 'Jim', age: 30, city: 'London' },
  { name: 'Bob', age: 27, city: 'Paris' }
];
// // Define the HTML template
var template = `
  <!DOCTYPE html>
  <html>
    <head>
      <title>People</title>
      <style>
        table {
          border-collapse: collapse;
        }
        td, th {
          border: 1px solid black;
          padding: 5px;
        }
      </style>

    </head>
    <body>
      <table>
        <tr>
          <th>Name</th>
          <th>Age</th>
          <th>City</th>
        </tr>
        ${people.map(function(person) {
          return `
            <tr>
              <td>${person.name}</td>
              <td>${person.age}</td>
              <td>${person.city}</td>
            </tr>
          `;
        }).join('')}
      </table>
    </body>
  </html>
`;
// // Import the fs module
var fs = require('fs');
// Write the HTML template to a file
fs.writeFile('dynamic.html', template, function(error) {
  if (error) {
    console.log(error.message);
  } else {
    console.log('File created successfully!');
  }
});

// `show this file in browser`
// Path: p4_6.js
// // Import the http module
var http = require('http');
// Import the fs module
var fs = require('fs');
// Create a server
http.createServer(function(request, response) {
  // Read the HTML file
  fs.readFile('dynamic.html', function(error, data) {
    // Write the contents of the file to the response
    response.write(data);
    // End the response
    response.end();
  });
}
).listen(8080);
`run this file in terminal and open browser with localhost:8080`


