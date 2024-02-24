<?php
    echo "21012011074<br><br>";
    $n = 10;
    $arr1 = [];
    $arr2 = [];
    for($i=0;$i<$n;$i++){
        $arr1[$i] = rand(1,50);
    }
    for($i=0;$i<$n;$i++){
        $arr2[$i] = rand(1,50);
    }
    echo "Before Sorting arr1: ";
    foreach($arr1 as $temp){
        echo "$temp, ";
    }
    echo "<br>Before Sorting arr2: ";
    foreach($arr2 as $temp){
        echo "$temp, ";
    }
    echo "<br>";
    function insertionSort(&$arr,$n){
        for($i=0;$i<$n;$i++){
            $j = $i;
            while($j>0 && $arr[$j-1]>$arr[$j]){
                $temp = $arr[$j];
                $arr[$j] = $arr[$j-1];
                $arr[$j-1] = $temp;
                $j--;
            }
        }
    }
    echo "<br>Sorting Arr1 without inbuilt function: ";
    insertionSort($arr1,$n);
    foreach($arr1 as $temp){
        echo "$temp, ";
    }

    echo "<br>Sorting Arr2 with inbuilt function: ";
    sort($arr2);
    foreach($arr2 as $temp){
        echo "$temp, ";
    }
?>