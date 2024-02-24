<!-- let range is 1 to 100 -->
<?php 
    $start=2;
    $end=100;
    for($i=$start;$i<=$end;$i++){
        $count=0;
        for($j=1;$j<=$i;$j++){
            if($i%$j==0){
                $count++;
            }
        }
        if($count==2){
            echo $i." ";
        }
    }

?>