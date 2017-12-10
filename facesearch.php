<?php

include 'api.php';

ob_start();
print_r($_FILES);
    file_put_contents("log.txt", ob_get_clean(), FILE_APPEND);

if($_FILES["file-upload"]["tmp_name"])
{
  if(!$_FILES["file-upload"]["error"])
  {
    file_put_contents("log.txt", $_FILES["file-upload"]["tmp_name"], FILE_APPEND);
      unlink("test/test.jpg");
    move_uploaded_file($_FILES["file-upload"]["tmp_name"], "test/test.jpg");
  }
    else
    {
    file_put_contents("log.txt", "Error1", FILE_APPEND);
    }
}
else
{
    file_put_contents("log.txt", "Error2", FILE_APPEND);
}

$id =  python_api("test/test.jpg");

//$id = 447;

//echo $id;

//

include 'db.php';

?>

<html>
  <head>
    <link href="https://fonts.googleapis.com/css?family=Encode+Sans" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
    <link rel="stylesheet" href="res-search-page-style.css" type="text/css">
    <link rel="stylesheet" href="lightbox.css" type="text/css">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>

  <body>
      <div class="nav-bar">
        <div class="logo">
          <img src="images/logo.png" width="auto" height="70px">
        </div>
        <div style="display:none" class="name">  Guide Me </div>
      </div>
      <div class="search-results">

<?php

  $sql = "SELECT id,name,experience,rating,city FROM guide WHERE id= '$id'";
  $result = mysqli_query($link, $sql);

  if (mysqli_num_rows($result) > 0) {
    // output data of each row
    while($row = mysqli_fetch_assoc($result)) {
        echo'
        <div class="info-container">';

        $id = $row["id"];

        $city = $row["city"];

        $sql1 = "SELECT lang FROM lang WHERE guide_id= '$id'";
        $result1 = mysqli_query($link, $sql1);

        $name = $row["name"];

        echo'<img src="png/face_'.$row["id"].'.png" width = "100%"> </img>';

        echo'<div class="info">
        <div class="details">
        <dl class="details-list">
        <h1 class="room-name">';

        echo $row["name"];

        echo '</h1>
        <dt> Ratings: </dt>
        <dd> <img  src="images/stars/';

        echo $row["rating"];

        echo '-star.png"></img>
        </dd> <hr>
        <dt>Experience:</dt>
        <dd>';

        echo $row["experience"];

        echo' years</dd><hr>
        <dt>City: </dt>
        <dd>';

        echo $city;

        echo '</dd>
        <hr><dt>Languages:</dt>
        <dd>';

        $l = array();
        while($row1 = mysqli_fetch_assoc($result1)) {
          $l[] = $row1["lang"];
        }

        echo implode(", ", $l);


        echo'</dd></dl></div>


        <div class="contact-btn-holder">
        <button type="button" class="contact-btn btn btn-primary">Contact Guide</button>

        </div>

        </form>

        </div>
        </div>';
    }
  }

  else {
    echo '<center> <p style="color:grey; font-size: 100px; opacity:0.5"> No Results Found... </p> </center>';
  }

  echo'
  </div>
  <script type="text/javascript" src="lightbox-plus-jquery.js"></script>

  </body>
  </html>';

  mysqli_close($link);

?>
