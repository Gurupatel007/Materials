<?php
require('db.php');
require 'C:/xampp/htdocs/guru/Prac-8/vendor/autoload.php"'; // path to the autoload file of PHPMailer
$con = OpenCon();
session_start();

if (isset($_POST['email'])) {
    $email = stripslashes($_REQUEST['email']);
    $email = mysqli_real_escape_string($con, $email);

    // check if email exists in the database
    $query = "SELECT * FROM `students` WHERE email='$email'";
    $result = mysqli_query($con, $query) or die(mysqli_error($con));
    $rows = mysqli_num_rows($result);

    if ($rows == 1) {
        // generate a unique token
        $token = bin2hex(random_bytes(50));

        // store token in the database
        $query = "UPDATE `students` SET token='$token' WHERE email='$email'";
        $result = mysqli_query($con, $query) or die(mysqli_error($con));

        // send email to user with the token in a link they can click on
        $to = $email;
        $subject = "Reset your password on example.com";
        // $msg = "Hi there, click on this <a href=\"new_password.php?token=" . $token . "\">link</a> to reset your password on our site";
        $msg = "Hi there, click on this <a href=\"http://" . $_SERVER['HTTP_HOST'] . "/guru/Prac-8/Login_Module/new_password.php?token=" . $token . "\">link</a> to reset your password on our site";
        $msg = wordwrap($msg, 70);

        $mail = new PHPMailer\PHPMailer\PHPMailer();
        $mail->isSMTP();
        $mail->SMTPAuth = true;
        $mail->SMTPSecure = 'ssl';
        $mail->Host = 'smtp.gmail.com';
        $mail->Port = '465';
        $mail->isHTML();
        $mail->Username = 'gurupatel21@gnu.ac.in'; // replace with your email
        $mail->Password = 'gnlu agxp scqs xecw'; // replace with your password
        $mail->SetFrom('no-reply@example.com');
        $mail->Subject = $subject;
        $mail->Body = $msg;
        $mail->AddAddress($to);

        if(!$mail->send()) {
            echo 'Message could not be sent.';
            echo 'Mailer Error: ' . $mail->ErrorInfo;
        } else {
            echo 'Message has been sent';
        }
    } else {
        echo "No user with that email address exists.";
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
            height: 40px;
            margin-bottom: 25px;
            padding: 0 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        
        .login-button {
            width: 100%;
            height: 40px;
            background: #007bff;
            border: 1px solid #007bff;
            border-radius: 5px;
            color: #fff;
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
    <form class="form" method="post" name="forgot_password">
        <h1 class="login-title">Forgot Password</h1>
        <input type="email" class="login-input" name="email" placeholder="Email Address" required>
        <input type="submit" value="Reset Password" name="submit" class="login-button">
    </form>
</body>
</html>