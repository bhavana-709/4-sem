<?php
// Division by zero
function divide($numerator, $denominator) {
    if ($denominator == 0) {
        throw new Exception("Cannot divide by zero.");
    }
    return $numerator / $denominator;
}

// Date format check
function checkDateFormat($date, $format = 'Y-m-d') {
    $dateTime = DateTime::createFromFormat($format, $date);
    if (!$dateTime || $dateTime->format($format) != $date) {
        throw new Exception("Invalid date format.");
    }
    echo "The date " . $date . " is valid.<br>";
    return true;
}

// Testing
try {
    echo divide(10, 2) . "<br>"; // Works
    echo divide(10, 0) . "<br>"; // Throws exception
} catch (Exception $e) {
    echo "Division error: " . $e->getMessage() . "<br>";
}

try {
    checkDateFormat("2023-03-10"); // Works
    checkDateFormat("10/03/2023"); // Throws exception
} catch (Exception $e) {
    echo "Date error: " . $e->getMessage() . "<br>";
}
?>
