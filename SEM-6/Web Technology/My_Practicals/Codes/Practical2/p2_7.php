<!-- Write a PHP program to print fibonacci series with and without using recursion and
check which method is efficient.
[Note: microtime() function is an inbuilt function in PHP which is used to return the
current Unix timestamp with microseconds.]
 -->
<?php
    function wihtoutRecursion($n){
        $a = 1;
        $b = 1;
        echo $a." ".$b," ";
        for($i=2;$i<$n;$i++){
            $c = $a+$b;
            echo $c." ";
            $a = $b;
            $b = $c;
        }
    }
    function withRecursion($n){
        if($n==0 || $n==1){
            return 1;
        }
        else{
            return (withRecursion($n-1)+withRecursion($n-2));
        }
    }

    // check which method is efficient.
    // [Note: microtime() function is an inbuilt function in PHP which is used to return the
    // current Unix timestamp with microseconds.]

    $start = microtime(true);
    wihtoutRecursion(8);
    $end = microtime(true);
    echo "<br>Time taken without recursion: ".($end-$start);
    $time_without_recursion = $end-$start;
    echo "<br>";
    $start = microtime(true);
    for($i=0;$i<8;$i++){
        echo withRecursion($i)." ";
    }
    $end = microtime(true);
    echo "<br>Time taken with recursion: ".($end-$start);
    $time_with_recursion = $end-$start;
    echo "<br>";    

    if($time_without_recursion < $time_with_recursion){
        echo "Without recursion is efficient";
    }
    else{
        echo "With recursion is efficient";
    }
?>