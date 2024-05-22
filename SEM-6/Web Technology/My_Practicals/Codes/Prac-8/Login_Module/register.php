<?php
require('db.php');
$con = OpenCon();
// When form submitted, insert values into the database.
if (isset($_REQUEST['enrollment'])) {
    // removes backslashes
    $enrollment = stripslashes($_REQUEST['enrollment']);
    //escapes special characters in a string
    $enrollment = mysqli_real_escape_string($con, $enrollment);
    $name = stripslashes($_REQUEST['name']);
    $name = mysqli_real_escape_string($con, $name);
    $branch = stripslashes($_REQUEST['branch']);
    $branch = mysqli_real_escape_string($con, $branch);
    $password = stripslashes($_REQUEST['password']);
    $password = mysqli_real_escape_string($con, $password);
    $email = stripslashes($_REQUEST['email']);
    $email = mysqli_real_escape_string($con, $email);

    // Handle the photo upload
    $photo = $_FILES['photo'];
    $photoPath = "uploads/" . basename($photo["name"]);

    if (move_uploaded_file($photo["tmp_name"], $photoPath)) {
        echo "File uploaded successfully.";
    } else {
        echo "File upload failed.";
    }

    $query    = "INSERT into `students` (enrollment, name, branch, password, photo, email)
                     VALUES ('$enrollment', '$name', '$branch', '" . md5($password) . "', '$photoPath', '$email')";
    $result   = mysqli_query($con, $query);
    if ($result) {
        echo "<div class='form'>
              <h3>You are registered successfully.</h3><br/>
              <p class='link'><a href='login.php'>Login</a></p>
              </div>";
    } else {
        echo "<div class='form'>
              <h3>Required fields are missing.</h3><br/>
              <p class='link'>Click here to <a href='registration.php'>registration</a> again.</p>
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
            color: #007bff;
            text-align: center;
            margin-top: 30px;
            font-size: 18px;
        }

        .link a {
            text-decoration: none;
            color: #007bff;
        }

        .link a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
<form class="form" action="" method="post" enctype="multipart/form-data">
        <h1 class="login-title">Registration</h1>
        <input type="text" class="login-input" name="enrollment" placeholder="Enrollment" required />
        <input type="text" class="login-input" name="name" placeholder="Name" required />
        <input type="text" class="login-input" name="branch" placeholder="Branch" required />
        <input type="password" class="login-input" name="password" placeholder="Password" required />
        <input type="email" class="login-input" name="email" placeholder="Email" required />
        <input type="file" class="login-input" name="photo" required />
        <input type="submit" name="submit" value="Register" class="login-button" />
        <p class="link"><a href="login.php">Click to Login</a></p>
    </form>
</body>
</html>
<?php
}
?>