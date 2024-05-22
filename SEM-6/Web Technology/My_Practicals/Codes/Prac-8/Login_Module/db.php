<?php
function OpenCon()
{
    $host = "localhost:3307"; /* Host name */
    $user = "root"; /* User */
    $password = ""; /* Password */
    $dbname = "studentmanagementsystem"; /* Database name */

    $con = new mysqli($host, $user, $password, $dbname) or die("Connect failed: %s\n". $con -> error);
    return $con;
}

function CloseCon($con)
{
    $con -> close();
}
?>