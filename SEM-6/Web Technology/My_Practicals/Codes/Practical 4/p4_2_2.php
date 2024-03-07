<?php
$name = isset($_POST["name"]) ? htmlspecialchars($_POST["name"]) : '';
$phone = isset($_POST["phone"]) ? htmlspecialchars($_POST["phone"]) : '';
$twisties = isset($_POST["twisties"]) ? intval($_POST["twisties"]) : 0;
$cadbury = isset($_POST["cadbury"]) ? intval($_POST["cadbury"]) : 0;
$cadburyNut = isset($_POST["cadburyNut"]) ? intval($_POST["cadburyNut"]) : 0;
$cloud9 = isset($_POST["cloud9"]) ? intval($_POST["cloud9"]) : 0;
$payment = isset($_POST["payment"]) ? htmlspecialchars($_POST["payment"]) : '';

$twisties_total = $twisties * 3.00;
$cadbury_total = $cadbury * 3.50;
$cadburyNut_total = $cadburyNut * 4.50;
$cloud9_total = $cloud9 * 0.30;

$total = $twisties_total + $cadbury_total + $cadburyNut_total + $cloud9_total;
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
        <tr>
            <td class="product-det">Twisties</td>
            <td class="product-price">RM 3.00</td>
            <td class="product-quantity"><?php echo $twisties; ?></td>
            <td class="product-subtotal">RM <?php echo $twisties_total; ?></td>
        </tr>
        <tr>
            <td class="product-det">Cadbury's Chocolate</td>
            <td class="product-price">RM 3.50</td>
            <td class="product-quantity"><?php echo $cadbury; ?></td>
            <td class="product-subtotal">RM <?php echo $cadbury_total; ?></td>
        </tr>
        <tr>
            <td class="product-det">Cadbury's Nut Chocolate</td>
            <td class="product-price">RM 4.50</td>
            <td class="product-quantity"><?php echo $cadburyNut; ?></td>
            <td class="product-subtotal">RM <?php echo $cadburyNut_total; ?></td>
        </tr>
        <tr>
            <td class="product-det">Cloud 9</td>
            <td class="product-price">RM 0.30</td>
            <td class="product-quantity"><?php echo $cloud9; ?></td>
            <td class="product-subtotal">RM <?php echo $cloud9_total; ?></td>
        </tr>
    </table>
    <table>
        <tr>
            <td>Total:</td>
            <td>RM <?php echo $total; ?></td>
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