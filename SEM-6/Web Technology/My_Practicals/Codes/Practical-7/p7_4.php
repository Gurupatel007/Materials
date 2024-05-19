<!-- Write a PHP program to create ‘customer feedback form’ and store data 
into Customer table. -->
<!DOCTYPE html>
<html>

<body>
    <form method="post">
        Enter Customer Name: <input type="text" name="cname"><br>
        Enter Item Purchased: <input type="text" name="item"><br>
        Enter Review: <input type="text" name="review"><br>
        <input type="submit" name="submit" value="Submit">
    </form>
    <?php
    if (isset($_POST['submit'])) {
        $cname = $_POST['cname'];
        $item = $_POST['item'];
        $review = $_POST['review'];
        $conn = mysqli_connect("localhost:3307", "root", "", "customers");
        if ($conn) {
            $sql = "INSERT INTO customer(C_name, Name_Item_purchased, review_product) VALUES('$cname', '$item', '$review')";
            if (mysqli_query($conn, $sql)) {
                echo "Data inserted successfully";
            } else {
                echo "Error inserting data:" . mysqli_error($conn);
            }
            mysqli_close($conn);
        } else {
            die("Connection failed: " . mysqli_connect_error());
        }
    }
    ?>
</body>

</html>