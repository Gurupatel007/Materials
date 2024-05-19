<?php
$connect = mysqli_connect("localhost:3307", "root", "","student");
if($connect){
    echo " connection established";
    $sql = 'CREATE TABLE customer (
        C_id INT,
        C_NAME VARCHAR(150),
        Name_Item_Purchased VARCHAR(150),
        review_product VARCHAR(150)
    )';
    if(mysqli_query($connect, $sql)){
        echo "Table created successfully<br>";
    }
    else{
        echo "Error creating table: " . mysqli_error($connect);
    }  
}
else{
    echo "myswli_connect_error()";
}
?>