<?php
    $file = $_GET['file'];
    $file = "uploads/".$file;
    if(file_exists($file)){
        unlink($file);
        header("Location: p6_3.php");
    }
?>