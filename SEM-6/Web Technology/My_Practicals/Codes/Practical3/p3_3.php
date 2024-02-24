<?php
    echo "21012011074<br><br>";
    $n = 10;
    $arr = [];
    $arr1 = [];
    $arr2 = [];
    for($i=0;$i<$n;$i++){
        $arr[$i] = rand(1,50);
        $arr1[$i] = rand(1,30);
        $arr2[$i] = rand(1,20);
    }
    echo "Array1: <br>";
    foreach($arr as $temp){
        echo "$temp, ";
    }
    echo "<br>Array2: <br>"; 
    foreach($arr1 as $temp){
        echo "$temp, ";
    }
    echo "<br>Array3: <br>"; 
    foreach($arr2 as $temp){
        echo "$temp, ";
    }
    echo "<br><br>Merged Array wihout using function: <br>";
    function mergeTwoArrays(&$arr,&$arr1,$n){
        for($i=0;$i<$n;$i++){
            $arr[$n+$i] = $arr1[$i]; 
        }
        foreach($arr as $temp){
            echo "$temp, ";
        }
    }
    mergeTwoArrays($arr,$arr1,$n);

    echo "<br><br>Merged Array Using inbuilt function: <br>";
    $arr2 = array_merge($arr1,$arr2);
    foreach($arr2 as $temp){
        echo "$temp, ";
    }
?>