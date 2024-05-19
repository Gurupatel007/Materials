<?php
require('db.php');
$con = OpenCon();
session_start();
if (!isset($_SESSION['enrollment'])) {
    header("Location: login.php");
}
// When form submitted, update password in the database.
if (isset($_REQUEST['password'])) {
    $password = stripslashes($_REQUEST['password']);
    $password = mysqli_real_escape_string($con, $password);
    $query    = "UPDATE `students` SET password='" . md5($password) . "' WHERE enrollment='" . $_SESSION['enrollment'] . "'";
    $result = mysqli_query($con, $query) or die(mysqli_error($con));
    // if ($result) {
    //     echo "<div class='form'>
    //           <h3>Password changed successfully.</h3><br/>
    //           <p class='link'><a href='login.php'>Login</a></p>
    //           <p class='link'><a href='logout.php'>Logout</a></p>
    //           </div>";
    // } else {
    //     echo "<div class='form'>
    //           <h3>Required fields are missing.</h3><br/>
    //           <p class='link'>Click here to <a href='change_password.php'>Change Password</a> again.</p>
    //           </div>";
    // }
    if ($result) {
        echo "<div class='form'>
              <h3>Password changed successfully.</h3><br/>
              <p class='link'><a href='login.php'>Login</a></p>
              <p class='link'><a href='logout.php'>Logout</a></p>
              </div>";
    } else {
        echo "<div class='form'>
              <h3>Required fields are missing.</h3><br/>
              <p class='link'>Click here to <a href='change_password.php'>Change Password</a> again.</p>
              </div>";
    }

    echo "<style>
        body {
            font-family: 'Courier New', monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f8f9fa;
        }
        .form {
            width: 400px;
            padding: 20px;
            background-color: #e9ecef;
            border: 2px solid #6c757d;
            border-radius: 5px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
            text-align: center;
        }
        .link a {
            color: #007bff;
            text-decoration: none;
        }
    </style>";
} else {
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Change Password</title>
    <style>
        /* add best styles into this form */
        body {
            font-family: 'Courier New', monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f8f9fa;
        }
        .form {
            width: 400px;
            padding: 20px;
            background-color: #e9ecef;
            border: 2px solid #6c757d;
            border-radius: 5px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
            text-align: center;
        }
        .login-title {
            color: #495057;
            margin-bottom: 30px;
            text-align: center;
            font-size: 28px;
        }
        .login-input {
            width: calc(100% - 60px);
            height: 40px;
            margin-bottom: 25px;
            padding: 0 30px;
            border: 1px solid #ced4da;
            border-radius: 4px;
            font-size: 18px;
        }
        .login-button {
            width: 100%;
            height: 40px;
            padding: 0;
            color: #fff;
            background: #007bff;
            border: 1px solid #007bff;
            border-radius: 4px;
            cursor: pointer;
            font-size: 18px;
            transition: background 0.3s ease;
        }
        .login-button:hover {
            background: #0056b3;
        }

        .link {
            text-align: center;
        }

        
    </style>
</head>
<body>
<form class="form" action="" method="post">
        <h1 class="login-title">Change Password</h1>
        <input type="password" class="login-input" name="password" placeholder="New Password" required />
        <input type="submit" name="submit" value="Change Password" class="login-button" />
    </form>
</body>
</html>
<?php
}
?>