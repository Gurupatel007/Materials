<?php
    echo "21012011074<br><br>";
    $n = 10;
    $arr1 = [];
    for($i=0;$i<$n;$i++){
        $arr1[$i] = rand(1,20);
    }
    echo "Array: ";
    foreach($arr1 as $temp){
        echo "$temp, ";
    }
    echo "<br>";
    function searchElement($arr,$n,$element){
        for($i=0;$i<$n;$i++){
            if($arr[$i]==$element){
                return $i;
            }
        }
        return -1;
    }
    $element = 14;
    $index = searchElement($arr1,$n,$element);
    if($index==-1){
        echo "Element not found";
    }else{
        echo "Firstly Element found at index: $index";
    }
    $frequency = 0;
    for($i=0;$i<$n;$i++){
        if($arr1[$i]==$element){
            $frequency++;
        }
    }
    echo "<br>Frequency of $element: $frequency";
?>