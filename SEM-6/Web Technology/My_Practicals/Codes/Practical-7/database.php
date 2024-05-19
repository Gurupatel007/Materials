<?php
$connect = mysqli_connect("localhost:3307", "root", "");
if($connect){
    echo " connection established";
    $sql = "CREATE DATABASE student";
    if(mysqli_query($connect, $sql)){
        echo "Database created successfully<br>";
    }
    else{
        echo "Error creating database: " . mysqli_error($connect);
    }
    mysqli_close($connect);
}
else{
    echo "myswli_connect_error()";
}
?>