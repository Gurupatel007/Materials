<?php
$name = isset($_POST["name"]) ? htmlspecialchars($_POST["name"]) : '';
$phone = isset($_POST["phone"]) ? htmlspecialchars($_POST["phone"]) : '';
$payment = isset($_POST["payment"]) ? htmlspecialchars($_POST["payment"]) : '';
$total = 0;
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order Summary</title>
    <link rel="stylesheet" href="./style2.css">
</head>
<body>
    <div class="container">
    <h1 class="main-title">Order Summary</h1>
    <table>
        <tr>
            <td>Buyer's Name:</td>
            <td><?php echo $name; ?></td>
        </tr>
        <tr>
            <td>Mobile No:</td>
            <td><?php echo $phone; ?></td>
        </tr>
    </table>
    <table>
        <tr class="product">
            <th>Product Name</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Subtotal</th>
        </tr>
        <?php
            $fp = fopen("Product_Name.csv", "r");
            $count = 0;
            while(!feof($fp)){
                $a = fgetcsv($fp);
                $quantities = $_POST["item"];
                if (is_array($a) && isset($quantities[$count]) && $quantities[$count] > 0) {
                    echo "<tr><td>".$a[0]."</td>"; // Product Name
                    echo "<td>".$a[1]."</td>"; // Price
                    echo '<td>'.$quantities[$count].'</td>'; // Quantity
                    echo '<td>';
                    if (isset($a[1]) && is_numeric($a[1]) && is_numeric($quantities[$count])) {
                        $subtotal = $a[1] * $quantities[$count];
                        echo $subtotal;
                        $total += $subtotal;
                    }
                    echo '</td></tr>';
                }
                $count++;
            }
            fclose($fp);
        ?>
    </table>
    <table>
        <tr>
            <td>Total:</td>
            <td><?php echo $total; ?></td>
        </tr>
    </table>
    <table>
        <tr>
            <td>Payment Method:</td>
            <td><?php echo $payment; ?></td>
        </tr>
    </table>
    </div>
</body>
</html>