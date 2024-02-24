<!-- 2. Demonstrate different ways to write a PHP code.
1. Without any HTML markups
2. Embedding HTML markups in PHP code
3. Embedding PHP code in HTML
 -->

<!-- Without any HTML markups -->
<?php
// without any HTML markups
$var = "This is PHP code without any HTML markups";
echo nl2br("$var\n");
echo "This is echo function";
?>

<!-- 2. Embedding HTML markups in PHP code -->
<?php
// Embedding HTML markups in PHP code
echo "<h1>This is echo function</h1>";
// this function is used to output one or more strings
?>

<!-- 3. Embedding PHP code in HTML -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP EMMBEDDE IN HTML</title>
</head>
<body>
    <?php
        echo "This is echo function<br>";
        // this function is used to output one or more strings
        echo "<h1 style='color: red'>This is echo function</h1>";
    ?>
</body>
</html>