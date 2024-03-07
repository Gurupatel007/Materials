<?php
// Demonstrating $_POST
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['name'])) {
    echo "Hello, " . $_POST['name'] . "! (via POST)<br>";
}

// Demonstrating $_GET
if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET['age'])) {
    echo "You are " . $_GET['age'] . " years old. (via GET)<br>";
}

// Demonstrating $_REQUEST for both POST and GET
if (isset($_REQUEST['city'])) {
    echo "Your city is " . $_REQUEST['city'] . ". (via REQUEST)<br>";
}

// Demonstrating $_ENV
$_ENV['USER'] = 'GURU'; // Directly set the value in the $_ENV superglobal
$user = $_ENV['USER']; // Access the variable from the $_ENV superglobal
echo "Your username is $user (via ENV)<br>";

// Demonstrating $_SERVER
echo "Your server software is " . $_SERVER['SERVER_SOFTWARE'] . " (via SERVER)<br>";

// Demonstrating $_GLOBALS
$GLOBALS['globalVar'] = "This is a global variable.";
echo $GLOBALS['globalVar'] . " (accessed via GLOBALS)<br>";
?>

<!DOCTYPE html>
<html>
<body>

<h2>PHP Superglobals Example</h2>

<form method="post" action="<?php echo $_SERVER["PHP_SELF"];?>">
    Name: <input type="text" name="name">
    City (via POST): <input type="text" name="city">
    <input type="submit">
</form>

<p>Click the link below to submit an age via GET request:</p>

<form method="get" action="<?php echo $_SERVER["PHP_SELF"];?>">
    Age: <input type="text" name="age">
    City (via GET): <input type="text" name="city">
    <input type="submit">
</form>

</body>
</html>
