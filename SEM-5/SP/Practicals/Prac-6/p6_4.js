var m = require('mysql') 
var con = m.createConnection({ 
    host: 'localhost',
    user: 'root',
    password: '',
    port : "3307",
    database: 'Node_test'
}); 
 
con.connect(function (err) { 
    if (err) {
        console.error('Error connecting to MySQL database:', err); 
    }
    else {
         console.log('Connected to MySQL database');
         var s = 'select * from product';
         con.query(s, function (err1, res) {
            if (err1) {
                 console.error('Error connecting to display detail:', err1); 
            }
            else {                
                console.log('21012011074');                 
                console.log(res); 
            } 
        }) 
    } 
});
