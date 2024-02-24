<!-- 8. Write a PHP program to enter the numbers of rows and columns and in the next page
generate the table with given rows and cols. -->
<!DOCTYPE html>
<html>
    <head>
        <title>PHP program to generate table with given rows and cols</title>
    </head>
    <body>
        <form action="p2_8_1.php" method="post">
            <label for="rows">Enter the number of rows:</label>
            <input type="number" name="rows" id="rows" required>
            <br>
            <label for="cols">Enter the number of columns:</label>
            <input type="number" name="cols" id="cols" required>
            <br>
            <input type="submit" value="Generate Table">
        </form>
    </body>
</html>

