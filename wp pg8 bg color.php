<!DOCTYPE html>
<html>
  <head>
    <title>Color Change by Day</title>
    <?php
    $daysOfWeek = array(
      'Sunday'    =>
    '#FF5733', 'Monday' => '#33FF57', 'Tuesday' => '#3357FF', 'Wednesday' =>
    '#FFFF33', 'Thursday' => '#FF33FF', 'Friday' => '#33FFFF', 'Saturday' =>
    '#FF3333' ); $currentDay = date('l'); // 'l' returns full name of the day
    $backgroundColor = array_key_exists($currentDay, $daysOfWeek) ?
    $daysOfWeek[$currentDay] : '#FFFFFF'; ?>
    <style>
      body {
        background-color: <?= $backgroundColor ?>;
        font-family: Arial, sans-serif;
        color: #333;
        padding: 20px;
      }
    </style>
  </head>
  <body>
    <h1>
      Welcome! Today is
      <?= $currentDay ?>.
    </h1>
  </body>
</html>
