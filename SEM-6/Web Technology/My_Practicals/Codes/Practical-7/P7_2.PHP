<!-- Write a PHP Program to create database at run time by passing database 
name in text box.  -->
<!DOCTYPE html>
<html>

<body>
    <form method="post">
        Enter Database Name: <input type="text" name="dbname">
        <input type="submit" name="submit" value="Create">
    </form>
    <?php
    if (isset($_POST['submit'])) {
        $dbname = $_POST['dbname'];
        $conn = mysqli_connect("localhost:3307", "root", "");
        if ($conn) {
            $sql = "CREATE DATABASE $dbname";
            if (mysqli_query($conn, $sql)) {
                echo "Database $dbname created successfully";
            } else {
                echo "Error creating database:" . mysqli_error($conn);
            }
            mysqli_close($conn);
        } else {
            die("Connection failed: " . mysqli_connect_error());
        }
    }
    ?>
</body>

</html>