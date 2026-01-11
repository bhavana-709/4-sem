<?php
function generatePrimes($maxNumber) {
    echo "Prime numbers up to $maxNumber:<br>";
    for ($number = 2; $number <= $maxNumber; $number++) {
        $isPrime = true;
        for ($i = 2; $i <= sqrt($number); $i++) {
            if ($number % $i == 0) {
                $isPrime = false;
                break;
            }
        }
        if ($isPrime) {
            echo "$number ";
        }
    }
    echo "<br><br>";
}

function fibonacciSeries($numTerms) {
    $first = 0;
    $second = 1;
    echo "Fibonacci Series ($numTerms terms):<br>";
    for ($i = 0; $i < $numTerms; $i++) {
        echo "$first ";
        $next = $first + $second;
        $first = $second;
        $second = $next;
    }
    echo "<br><br>";
}

// Call the functions
generatePrimes(30);
fibonacciSeries(10);
?>
