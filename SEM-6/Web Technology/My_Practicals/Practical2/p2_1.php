<!-- 1. Study the following functions & write a description for each:
echo(), print(), phpinfo(), define(), var_dump(), date(), Time()
 -->

 <?php
    echo "This is echo function<br>";
    // this function is used to output one or more strings

    print("This is print function<br>");
    // this function is used to output one or more strings

    // phpinfo()
    // this function is used to output the information about the PHP configuration

    define("GREETING", "Welcome to W3Schools.com!<br>");
    echo GREETING;
    // this function is used to define a constant

    $x = 5985;
    var_dump($x);
    // this function is used to display structured information about one or more variables

    echo "<br>Today is " . date("Y/m/d") . "<br>";
    // this function is used to format a local time/date

    echo "The time is " . date("h:i:sa") . " <br>";
    // this function is used to format a local time/date

    echo "The time is " . time() . " <br>";
    // this function is used to return the current time in seconds


 ?>