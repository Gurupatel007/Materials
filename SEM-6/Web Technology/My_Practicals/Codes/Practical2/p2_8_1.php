<?php
    $rows = $_POST['rows'];
    $cols = $_POST['cols'];
    echo "<table border='1'>";
    for($i=0;$i<$rows;$i++){
        echo "<tr>";
        for($j=0;$j<$cols;$j++){
            echo "<td>Row $i, Col $j</td>";
        }
        echo "</tr>";
    }
    echo "</table>";
?>