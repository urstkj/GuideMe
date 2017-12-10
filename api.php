<?php

function python_api($filename)
{
    $ch = curl_init();
    $json = array();
    $json["photourl"] = $filename;
    $json = json_encode($json);
    //print_r($json);
    
    curl_setopt($ch, CURLOPT_URL,"http://localhost:5000/facerecognize");
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS,$json);
    curl_setopt($ch,CURLOPT_USERAGENT,'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13');
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt( $ch, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));
    $server_output = curl_exec ($ch);
    curl_close ($ch);
    
    $parse = json_decode($server_output, true);

    return $parse["id"];

}