<!-- Write  a  PHP  program  to  display  information  of  Customer  table  with 
well formatting (table form) on output screen.  -->
<?php
// Database connection parameters
$servername = "localhost:3307";
$username = "root";
$password = "";
$dbname = "customers";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// SQL query to select data from database
$sql = "SELECT * FROM Customer";
$result = $conn->query($sql);
$conn->close();

// Display data in a table
echo "<table border='1'>
<tr>
<th>C_Id</th>
<th>C_name</th>
<th>Name_Item_purchased</th>
<th>review_product</th>
</tr>";

while($row = mysqli_fetch_array($result))
{
echo "<tr>";
echo "<td>" . $row['C_Id'] . "</td>";
echo "<td>" . $row['C_name'] . "</td>";
echo "<td>" . $row['Name_Item_purchased'] . "</td>";
echo "<td>" . $row['review_product'] . "</td>";
echo "</tr>";
}
echo "</table>";
?>