<?php
// Get the current hour
$current_hour = date('G');
// cout<< date('G');
    echo date('G')."<br>";

// Determine the part of the day based on the current hour
if ($current_hour < 12) {
    echo "Good Morning";
} elseif ($current_hour < 18) {
    echo "Good Afternoon";
} else {
    echo "Good Evening";
}
?>