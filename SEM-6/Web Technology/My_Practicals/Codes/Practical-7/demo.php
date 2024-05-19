<?php
$servername = "localhost:3307";
$username = "root";
$password = "";
$database = "exam";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $database);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Query to fetch data
$sql = "SELECT * FROM student";
$result = mysqli_query($conn, $sql);

// Check if there are any rows in the result
if (mysqli_num_rows($result) > 0) {
    // Output data of each row
    echo "<table border='1'>";
    echo "<tr><th>ID</th><th>Name</th><th>Branch</th><th>City</th></tr>";
    while($row = mysqli_fetch_assoc($result)) {
        echo "<tr><td>".$row["s_id"]."</td><td>".$row["s_name"]."</td><td>".$row["s_branch"]."</td><td>".$row["s_city"].".</td></tr>";
    }
    echo "</table>";
} else {
    echo "0 results";
}

// Close connection
mysqli_close($conn);
?>
