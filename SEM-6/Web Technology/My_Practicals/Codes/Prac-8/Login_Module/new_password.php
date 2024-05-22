<?php
require('db.php');
$con = OpenCon();
session_start();

if (isset($_GET['token']) && isset($_POST['new_password'])) {
    $token = $_GET['token'];
    $new_password = stripslashes($_REQUEST['new_password']);
    $new_password = mysqli_real_escape_string($con, $new_password);

    // check if token exists in the database
    $query = "SELECT * FROM `students` WHERE token='$token'";
    $result = mysqli_query($con, $query) or die(mysqli_error($con));
    $rows = mysqli_num_rows($result);

    if ($rows == 1) {
        // update password in the database
        $query = "UPDATE `students` SET password='".md5($new_password)."', token='' WHERE token='$token'";
        $result = mysqli_query($con, $query) or die(mysqli_error($con));

        echo "Your password has been changed successfully.";
    } else {
        echo "Invalid token.";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <!-- ... -->
    <style>
        body {
            font-family: "Roboto", sans-serif;
            background: #f8f9fa;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        
        .form {
            width: 400px;
            padding: 40px 30px;
            background: #fff;
            border: 1px solid #ced4da;
            border-radius: 5px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
        }
        
        .login-title {
            color: #495057;
            margin-bottom: 30px;
        }
        
        .login-input {
            width: calc(100% - 20px);
        }
        
        .login-button {
            width: 100%;
            padding: 10px;
            margin-top: 20px;
            background: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        
        .login-button:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <form class="form" method="post" name="new_password">
        <h1 class="login-title">New Password</h1>
        <input type="password" class="login-input" name="new_password" placeholder="New Password" required>
        <input type="submit" value="Change Password" name="submit" class="login-button">
    </form>
</body>
</html>