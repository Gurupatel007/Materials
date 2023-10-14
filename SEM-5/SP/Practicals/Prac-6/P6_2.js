var con = require('mysql');

var conn = con.createConnection({
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'port': '3307',
    'database': 'Node_test'
});

conn.connect((err) => {
    if (err) {
        console.error('Error connecting to MySQL database:', err);
    } else {
        // console.log('Connected to MySQL database');

        var x = 'create table product (id int NOT NULL AUTO_INCREMENT, name varchar(20), brand varchar(20),quantity int ,price int, PRIMARY KEY (Personid))';

        conn.query(x, (err) => {
            if (err) {
                console.error('Error creating database:', err);
            } else {
                console.log('Table created successfully');
            }
            conn.end();
        });
    }
});
