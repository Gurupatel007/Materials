<?php
$connect = mysqli_connect("localhost:3307", "root", "","student");
if($connect){
    echo " connection established";
    $sql ='INSERT INTO customer (C_NAME, Name_Item_Purchased, review_product) VALUES ("Rahul", "Mobile", "Good")';
    if(mysqli_query($connect, $sql)){
        echo "Data inserted successfully<br>";
    }
    else{
        echo "Error creating table: " . mysqli_error($connect);
    }  
}
else{
    echo "myswli_connect_error()";
}
?>