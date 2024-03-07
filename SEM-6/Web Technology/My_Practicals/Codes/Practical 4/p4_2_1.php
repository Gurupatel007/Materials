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
                <td><input type="text" name="name" id="name"></td>
            </tr>
            <tr>
                <td>Mobile No:</td>
                <td><input type="tel" id="phone" name="phone" pattern="\+91[0-9]{10}" placeholder="+917963552563"></td>
            </tr>
        </table>
        <table>
            <tr></tr>
            <tr></tr>
            <tr class="product">
                <th>Product Name</th>
                <th>Price</th>
                <th>Quantity</th>
            </tr>
            <tr>
                <td class="product-det">Twisties</td>
                <td class="product-price">RM 3.00</td>
                <td class="product-quantity"><input type="number" name="twisties" id="twisties" min="0" max="10"></td>
            </tr>
            <tr>
                <td class="product-det">Cadbury's Chocolate</td>
                <td class="product-price">RM 3.50</td>
                <td class="product-quantity"><input type="number" name="cadbury" id="cadbury" min="0" max="10"></td>
            </tr>
            <tr>
                <td class="product-det">Cadbury's Nut Chocolate</td>
                <td class="product-price">RM 4.50</td>
                <td class="product-quantity"><input type="number" name="cadburyNut" id="cadburyNut" min="0" max="10"></td>
            </tr>
            <tr>
                <td class="product-det">Cloud 9</td>
                <td class="product-price">RM 0.30</td>
                <td class="product-quantity"><input type="number" name="cloud9" id="cloud9" min="0" max="10"></td>
            </tr>
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