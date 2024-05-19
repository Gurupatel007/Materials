<?php
require('db.php');
$con = OpenCon();
session_start();
// When form submitted, check and create user session.
if (isset($_POST['enrollment'])) {
    $enrollment = stripslashes($_REQUEST['enrollment']);    // removes backslashes
    $enrollment = mysqli_real_escape_string($con, $enrollment);
    $password = stripslashes($_REQUEST['password']);
    $password = mysqli_real_escape_string($con, $password);
    // Check user is exist in the database
    $query    = "SELECT * FROM `students` WHERE enrollment='$enrollment'
                     AND password='" . md5($password) . "'";
    $result = mysqli_query($con, $query) or die(mysqli_error($con));
    $rows = mysqli_num_rows($result);
    if ($rows == 1) {
        $_SESSION['enrollment'] = $enrollment;
        // Redirect to user dashboard page
        header("Location: dashboard.php");
    } else {
        echo "<div class='form'>
                  <h3>Incorrect Enrollment/password.</h3><br/>
                  <p class='link'>Click here to <a href='login.php'>Login</a> again.</p>
                  </div>";
    }
} else {
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body {
            font-family: "Roboto", sans-serif;
            background: #f8f9fa;
            display: flex;
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
            height: 40px;
            padding: 0 10px;
        }
        
        .login-input,
        .login-button {
            margin-bottom: 20px;
        }
        
        .login-button {
            width: 100%;
            height: 40px;
            background: #007bff;
            border: none;
            border-radius: 5px;
            color: #fff;
            font-size: 15px;
            cursor: pointer;
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
<!-- <form class="form" method="post" name="login">
        <h1 class="login-title">Login</h1>
        <input type="text" class="login-input" name="enrollment" placeholder="Enrollment" autofocus="true"/>
        <input type="password" class="login-input" name="password" placeholder="Password"/>
        <input type="submit" value="Login" name="submit" class="login-button"/>
      <p class="link"><a href="registration.php">New Registration</a></p>
  </form> -->
    <form class="form" method="post" name="login">
    <h1 class="login-title">Login</h1>
        <input type="text" class="login-input" name="enrollment" placeholder="Enrollment Number" autofocus="true" required>
        <input type="password" class="login-input" name="password" placeholder="Password" required>
        <input type="submit" value="Login" name="submit" class="login-button">
        <p class="link"><a href="forgot_password.php">Forgot Password?</a></p>
        <p class="link"><a href="register.php">New Registration</a></p>
    </form>
</body>
</html>
    
<?php
}
?>