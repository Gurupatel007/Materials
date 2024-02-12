<?php 
    $sum=0;
    $count=0;
    $i=1;
    while($count!=100){
        if($i%2!=0){
            $sum+=$i;
            $count++;
        }
        $i++;
    }
    echo $sum;
?>