//synchronous function concept
var fs = require('fs');
//var data = fs.readFileSync('demo.txt');
//console.log(data.toString());
//console.log("Program End");

// asynchronous using anonymous function
fs.readFile('demo.txt',function (err,data){
    if (err){
        return console.error(err);
    }
    console.log(data.toString());
});
console.log("program end");