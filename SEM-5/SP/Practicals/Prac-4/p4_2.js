// Import the fs module
var fs = require('fs');
// Define a function that takes a search term as input and searches for it in the file
function searchFile(term) {
  var data = fs.readFileSync('pra-4.txt', 'utf8');
  var lines = data.split('\n');
  for (var i = 0; i < lines.length; i++) {
    // Get the current line
    var line = lines[i];
    // Check if the line contains the search term
    if (line.includes(term)) {
      // Find the index of the first occurrence of the term in the line
      var index = line.indexOf(term);
      // Display the line number and position of the occurrence in the console
      console.log('Found "' + term + '" in line ' + (i + 1) + ', position ' + (index + 1));
    }
  }
}
// Call the function with the search term as an argument
searchFile('hello');
