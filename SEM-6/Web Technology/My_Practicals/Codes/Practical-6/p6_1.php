<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Form</title>

    <style>
        body {
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }
        .container{
            width: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        form {
            width:1000px;
            height: auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
        }
        input[type="text"], input[type="tel"], input[type="email"], textarea {
            margin: 0 auto;
            width: 80%;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 4px;
            border: 1px solid #ddd;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        .input-btn{
            margin: 0 auto;
            width: 80%;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 4px;
            border: 1px solid #ddd;
        }
    </style>
</head>
<body>
    <div class="container">
    <h1>Student Registration Form</h1>
    <form action="<?php $_SERVER['PHP_SELF'];?>" method="post" enctype="multipart/form-data">
        <label for="enrollment_no">Enrollment No.</label><br>
        <input type="text" name="enrollment_no" id="enrollment_no" required><br><br>
        <label for="full_name">Full Name</label><br>
        <input type="text" name="full_name" id="full_name" required><br><br>
        <label for="gender">Gender</label><br>
        <input type="radio" name="gender" id="gender" value="male"> Male
        <input type="radio" name="gender" id="gender" value="female"> Female<br><br>
        <label for="mobile">Mobile</label><br>
        <input type="tel" name="mobile" id="mobile" required><br><br>
        <label for="email">Email</label><br>
        <input type="email" name="email" id="email" required><br><br>
        <label for="address">Address</label><br>
        <textarea name="address" id="address" rows="7" required></textarea><br><br>
        <label for="photo">Profile Photo</label><br>
        <input type="file" name="photo" id="photo" class="input-btn" required><br><br>
        <input type="submit" value="Submit">
    </form>
    </div>
</body>
</html>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $enrollment_no = $_POST["enrollment_no"];
    $full_name = $_POST["full_name"];
    $gender = $_POST["gender"];
    $mobile = $_POST["mobile"];
    $email = $_POST["email"];
    $address = $_POST["address"];
    $photo = $_FILES["photo"]["name"];

    // Validate inputs
    if (!preg_match("/^[a-zA-Z-' ]*$/", $full_name)) {
        echo "Only letters and white space allowed in Full Name";
        exit;
    }
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Invalid email format";
        exit;
    }
    if (!preg_match("/^[0-9]{10}$/", $mobile)) {
        echo "Invalid mobile number";
        exit;
    }
    if ($_FILES["photo"]["size"] > 500000) {
        echo "Sorry, your file is too large.";
        exit;
    }

    // Store data in CSV file
    $file = fopen('students.csv', 'a');
    fputcsv($file, array($enrollment_no, $full_name, $gender, $mobile, $email, $address, $photo));
    fclose($file);

    // Move uploaded file to a directory
    // move_uploaded_file($_FILES["photo"]["tmp_name"], "uploads/" . $photo);
    $target_file = "uploads/" . $photo;
    if (move_uploaded_file($_FILES["photo"]["tmp_name"], $target_file)) {
        echo "The file ". htmlspecialchars(basename($photo)). " has been uploaded.";
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
    echo "<br>Registration successful!";
}
?>