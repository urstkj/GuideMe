<?php

print_r($_POST);

include 'db.php';


/*
Array
(
    [city] => Ahmedabad
    [name] => Yash
    [languages] => Hindi,English
    [exp] => 6
    [id] => 100
)
*/

extract($_POST);

$sql = "INSERT INTO `guide` (`id`, `name`, `city`, `experience`, `rating`)
VALUES ('{$id}', '{$name}', '{$city}', '{$exp}', '0');";

$l = explode(",", $languages);

$res = mysqli_query($link, $sql);

if($res)
{
    foreach($l as $a)
    {
        $ss = "INSERT INTO `lang` (`guide_id`, `lang`)
                VALUES ('{$id}', '{$a}');";
        
        $result = mysqli_query($link, $ss);
        
        if(!$result)
        {
            echo "0";
            exit();
        }
    }

    echo "1";
}
else
{
    echo "0";
}