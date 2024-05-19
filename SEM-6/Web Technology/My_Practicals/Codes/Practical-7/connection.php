<?php
$connect = mysqli_connect("localhost:3307", "root", "");
if($connect){
    echo " connection established";
    
}
else{
    echo "myswli_connect_error()";
}
?>