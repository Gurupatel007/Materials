<?php
    echo "21012011074<br><br>";
    $n = 10;
    $arr1 = [];
    $arr2 = [];
    for($i=0;$i<$n;$i++){
        $arr1[$i] = rand(1,20);
    }
    for($i=0;$i<$n;$i++){
        $arr2[$i] = rand(1,20);
    }
    echo "Array1: ";
    foreach($arr1 as $temp){
        echo "$temp, ";
    }
    echo "<br>Array2: ";
    foreach($arr2 as $temp){
        echo "$temp, ";
    }
    echo "<br>";
    function removeDuplicates(&$arr,$n){
        $temp = [];
        $j = 0;
        for($i=0;$i<$n;$i++){
            if(!in_array($arr[$i],$temp)){
                $temp[$j] = $arr[$i];
                $j++;
            }
        }
        $arr = $temp;
    }
    removeDuplicates($arr1,$n);
    echo "<br>Array after removing duplicates without inbuit function: ";
    foreach($arr1 as $temp){
        echo "$temp, ";
    }

    echo "<br>Array after removing duplicates with inbuit function: ";
    $arr2 = array_unique($arr2);
    foreach($arr2 as $temp){
        echo "$temp, ";
    }
?>