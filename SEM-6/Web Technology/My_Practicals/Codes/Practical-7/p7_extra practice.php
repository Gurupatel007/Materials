<!DOCTYPE html>
<html>
<head>
    <title>Extra Practice</title>
    <style>
        body {
            background-color: #f1f1f1;
            font-family: Arial, sans-serif;
        }
        form {
            background-color: #fff;
            padding: 20px;
            margin: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input[type="text"], input[type="number"], input[type="submit"] {
            padding: 5px;
            margin: 5px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <form method="post">
        Enter Table Name: <input type="text" name="tablename">
        Enter Number of Fields: <input type="number" name="numfields">
        <input type="submit" name="submit" value="Create">
    </form>
    <?php
    if (isset($_POST['submit'])) {
        $tablename = $_POST['tablename'];
        $numfields = $_POST['numfields'];
        echo "<form method='post'>";
        echo "<input type='hidden' name='tablename' value='$tablename'>";
        for ($i = 1; $i <= $numfields; $i++) {
            echo "Field $i Name: <input type='text' name='fieldname$i'>";
            echo "Field $i Type: <input type='text' name='fieldtype$i'>";
            echo "Field $i Size: <input type='text' name='fieldsize$i'><br>";
        }
        echo "<input type='submit' name='createsubmit' value='Create Table'>";
        echo "</form>";
    }
    if (isset($_POST['createsubmit'])) {
        $servername = "localhost:3307";
        $username = "root";
        $password = "";
        $dbname = "customers";
        $conn = new mysqli($servername, $username, $password, $dbname);
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }
        $tablename = $_POST['tablename'];
        $i = 1;
        $fields = ["id INT AUTO_INCREMENT PRIMARY KEY"];
        while(isset($_POST["fieldname$i"])) {
            $fieldname = trim($_POST["fieldname$i"]);
            $fieldtype = trim($_POST["fieldtype$i"]);
            $fieldsize = trim($_POST["fieldsize$i"]);
            $fields[] = "$fieldname $fieldtype($fieldsize)";
            $i++;
        }
        $sql = "CREATE TABLE $tablename (" . implode(", ", $fields) . ")";
        if ($conn->query($sql) === TRUE) {
            echo "Table $tablename created successfully";
        } else {
            echo "Error creating table: " . $conn->error;
        }
        $conn->close();
    }
    ?>
</body>
</html>