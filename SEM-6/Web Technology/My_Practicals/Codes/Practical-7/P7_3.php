<!-- Write  a  PHP  Program  to  create  Customer  table  at  run  time  with  C_Id, 
C_name, Name_Item_purchased and review_product fields. -->
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
        $conn = mysqli_connect("localhost:3307", "root", "", $dbname);
        if ($conn) {
            $sql = "CREATE TABLE Customer(C_Id INT(6) AUTO_INCREMENT PRIMARY KEY, C_name VARCHAR(30) NOT NULL, Name_Item_purchased VARCHAR(30) NOT NULL, review_product VARCHAR(30) NOT NULL)";
            if (mysqli_query($conn, $sql)) {
                echo "Table Customer created successfully";
            } else {
                echo "Error creating table:" . mysqli_error($conn);
            }
        } else {
            die("Connection failed: " . mysqli_connect_error());
        }
        mysqli_close($conn);
    }

    ?>
</body>

</html>