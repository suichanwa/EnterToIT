<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
  <form method="POST">
    <p>ASP.NET: <input type="checkbox" name="technologies[]" value="ASP.NET" /></p>
    <p>PHP: <input type="checkbox" name="technologies[]" value="PHP" /></p>
    <p>Node.js: <input type="checkbox" name="technologies[]" value="Node.js" /></p>
    <input type="submit" value="Отправить">
</form> 

<form defined="fileUpdate.php" method="POST" >
    <input type="submit" value="Отправить">
</form>

<form method="post" enctype="multipart/form-data">
    <input type="file" name="file" size="10">
    <input type="submit" value="Отправить">
</form>



</body>
</html>


<?php

if(isset($_POST['users'])){
    $firstname = $_POST['firstname'];
    $secondUser = $_POST['secondUser'];
    
    echo $firstname . " " . $secondUser;
}

if(isset($_POST['technologies'])){
    $technologies = $_POST['technologies'];
    echo "<pre>";
    print_r($technologies);
    echo "</pre>";


    foreach($technologies as $item){
        echo "$item . <br>";
    }
}

//create a fucntion that will send user to fileUpload.php
function redirect($file){
    header("Location: $file");
}

redirect('fileUpload.php');

function uploadFile($file){
    //check if file is uploaded
    if(is_uploaded_file($file['tmp_name'])){
        //move file from temp location to the folder
        move_uploaded_file($file['tmp_name'], 'uploads/' . $file['name']);
    }
}

?>