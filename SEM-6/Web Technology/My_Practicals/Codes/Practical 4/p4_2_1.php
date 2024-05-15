<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./styles.css">
</head>
<body>
    <div class="container">
    <h1 class="main-title">Welcome to U-Shop @GUNI</h1>
    <form action="./p4_2_2.php" method = "post">
        <table>
            <tr>
                <td>Buyer's Name:</td>
                <td><input type="text" name="name" id="name" required></td>
            </tr>
            <tr>
                <td>Mobile No:</td>
                <td><input type="tel" id="phone" name="phone" pattern="\+91[0-9]{10}" placeholder="+917963552563" required></td>
            </tr>
        </table>
        <table>
            <tr class="product">
                <th>Product Name</th>
                <th>Price</th>
                <th>Quantity</th>
            </tr>
            <?php
                $fp = fopen("Product_Name.csv", "r");
                while(!feof($fp)){
                    $a = fgetcsv($fp);
                    if (is_array($a)) {
                        $i = 0;
                        $count = 0;
                        echo "<tr><td>".$a[$i]."</td>";
                        $i++;
                        echo "<td>".$a[$i]."</td>";
                        $i++;
                        echo '<td><input type="number" value="0" name="item[]" id="item.$count" min="0" max="10"></td>';
                        $count++;
                        echo "</tr>";
                    }
                }
            ?>

        </table>
        
        <div class="payment-method">
            <h2>Payment Method</h2>
            <input type="radio" name="payment" value="cash">Cash<br>
            <input type="radio" name="payment" value="visa">Visa<br>
            <input type="radio" name="payment" value="master">Master<br>
        </div>
        
        <div class="buttons">
            <input type="submit" value="Submit Order">
            <input type="reset" value="Cancel Order">
        </div>
    </form>
    </div>
</body>
</html>