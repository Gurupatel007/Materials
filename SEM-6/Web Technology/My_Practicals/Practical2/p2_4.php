<?php
function daysInMonth($month) {
    // Array of days in each month
    $days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    // Return the number of days in the given month
    return $days_in_month[$month - 1];
}

// Test the function
echo daysInMonth(6);  // Outputs: 30
?>