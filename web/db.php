<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "guide";


$link = mysqli_connect($servername, $username, $password, $dbname);

if ($link === false) {
    die("Connection failed: " . mysqli_connect_error());
}

?>
