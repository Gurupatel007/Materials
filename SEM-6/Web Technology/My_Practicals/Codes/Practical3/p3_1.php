<?php
    echo "21012011074<br><br>";
    $n = 10;
    $arr = [];
    for($i=0;$i<$n;$i++){
        $arr[$i] = rand(1,50);
    }
    // let max = arr[0];
    foreach($arr as $temp){
        echo "$temp ";
    }
    echo "<br>";
    function maxAndMin(&$arr,$n){
        $max = $arr[0];
        $min = $arr[0];
        for($i=1;$i<$n;$i++){
            if($arr[$i]>$max){
                $max = $arr[$i];
            }
            if($arr[$i]<$min){
                $min = $arr[$i];
            }
        }
        echo "The maxiumum element: ",$max,"<br>";
        echo "The minimum element: ",$min;
    }
    echo "<br> Without using inbuilt function: ";
    maxAndMin($arr,$n);

    echo "<br><br>Using inbuilt functions: ";
    echo "Maximum Element: ",max($arr),"<br>";
    echo "Minimum Element: ",min($arr);
?>