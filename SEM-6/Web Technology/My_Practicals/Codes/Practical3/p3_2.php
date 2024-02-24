<?php
    echo "21012011074<br><br>";
    $n = 10;
    $arr = [];
    for($i=0;$i<$n;$i++){
        $arr[$i] = rand(1,50);
    }
    echo "Before reverse: ";
    foreach($arr as $temp){
        echo "$temp, ";
    }
    echo "<br>";
    function swap(&$arr,$start,$end){
        $temp = $arr[$start];
        $arr[$start] = $arr[$end];
        $arr[$end] = $temp;
    }
    function reverse(&$arr,$n){
        $start=0;
        $end = $n-1;
        while($start<=$end){
            swap($arr,$start,$end);
            $start++;
            $end--;
        }
    }
    reverse($arr,$n);
    echo "<br>Without inbuilt function: ";
    foreach($arr as $temp){
        echo "$temp, ";
    }

    echo "<br>Using inbuilt function: ";
    array_reverse($arr);
    foreach($arr as $temp){
        echo "$temp, ";
    }
?>