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
session_start();
echo session_id();
echo session_name();
echo $_COOKIE["PHPSESSION"];


try{
    $db = new PDO('mysql:host=localhost;dbname=test', 'root', '');
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
}
catch(PDOException $e){
    echo $e->getMessage();
}


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

function redirect($file){
    header("Location: $file");
}

redirect('fileUpload.php');

function uploadFile($file){
    if(is_uploaded_file($file['tmp_name'])){
        move_uploaded_file($file['tmp_name'], 'uploads/' . $file['name']);
    }
}

?>
