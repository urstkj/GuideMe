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

<html>
  <head>
    <link href="https://fonts.googleapis.com/css?family=Encode+Sans" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="style.css">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">

  </head>

  <body>
    <div class="nav-bar">
      <div class="logo">
        <img src="images/logo.png" width="auto" height="70px">
      </div>
      <div style="display:none" class="name">  Guide Me </div>
    </div>
    <div class="container">
      <center>
        <form action="search-page.php"  method="post" name="f"    enctype="multipart/form-data">
          <div class="search-bar input-group">
            <input id="auto" list="area-list" name="city" type="text" class="search-input form-control" placeholder="Search City..." autocomplete="off">
            <datalist id="area-list"></datalist>
            <span class="search-btn-holder input-group-btn">
                <button name="submit" type="submit" class="btn btn-primary btn-secondary search-btn " type="button">Search</button>
            </span>
          </div>
        </form>
        <div class="select-type">
          <form id="guide-search" action="facesearch.php"  method="post" name="f"  enctype="multipart/form-data">
            <button type="button" id="face-search" class="select-btn btn btn-primary">Face Search</button>
            <input type="file" id="file-upload" name="file-upload" hidden/>
            <input type="submit" id="submit-btn" hidden/>
          </form>
        </div>
      </center>
    </div>

<?php
    $sql = "SELECT DISTINCT city FROM guide";
    $result = mysqli_query($link, $sql);

    $Areas = array();
?>
      <script>

      function sortByKey(array, key, dataList){

    	array.sort();
    	var length = array.length;
    	var keyLength = key.length;

    	var options = "";

    	for(var i=0; i<length; i++)
    	{
    		if(key === array[i].substring(0, keyLength)){
    			options += "<option value=" + array[i] + ">";
    		}
    	}

    	dataList.innerHTML = options;
    }

    var arr = [];

<?php

    if (mysqli_num_rows($result) > 0) {
      while($row = mysqli_fetch_assoc($result)) {
        echo 'arr.push("'.$row["city"].'");';
      }
    }
?>
        var auto = document.getElementById("auto");
        var dataList = document.getElementById("area-list");

        auto.oninput = function(){
        	var text = auto.value;
          text = text.charAt(0).toUpperCase() + (text.slice(1)).toLowerCase();
        	sortByKey( arr, text, dataList);
        };

        </script>
        <script src="upload.js"></script>
  </body>
</html>

<?php
  mysqli_close($link);
?>
