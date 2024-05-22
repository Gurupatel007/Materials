<?php

session_start();
if (!isset($_SESSION['enrollment'])) {
    header("Location: login.php");
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
    <style>
        body {
            font-family: 'Courier New', monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f8f9fa;
        }
        .container {
            width: 400px;
            padding: 20px;
            background-color: #e9ecef;
            border: 2px solid #6c757d;
            border-radius: 5px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
            text-align: center;
        }
        .welcome {
            color: #495057;
            margin-bottom: 30px;
            text-align: center;
            font-size: 28px;
        }
        button {
            width: 100%;
            height: 40px;
            background: #007bff;
            border: none;
            border-radius: 5px;
            color: #fff;
            font-size: 15px;
            cursor: pointer;
            margin: 10px 0;
        }
        button a {
            text-decoration: none;
            color: #fff;
        }
        button:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <p class="welcome">Welcome <?php echo $_SESSION['enrollment']; ?></p>
        <button><a href='change_password.php'>Change Password</a></button>
        <button><a href='logout.php'>Logout</a></button>
    </div>
</body>
</html>