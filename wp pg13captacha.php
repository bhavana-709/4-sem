<?php
session_start();

function generateCaptchaCode($length = 6) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}

// Generate and store the CAPTCHA in session
$captcha = generateCaptchaCode();
$_SESSION['captcha'] = $captcha;

echo "Captcha Code is: <strong>$captcha</strong>";
?>
