<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>


<form method="post" enctype="multipart/form-data">
    <input type="file" name="file" size="10">
    <input type="submit" value="Отправить">
</form>




</body>
</html>


<?php
//crate a function that will take and upload file 
function uploadFile($file){
    //check if file is uploaded
    if(is_uploaded_file($file['tmp_name'])){
        //move file from temp location to the folder
        move_uploaded_file($file['tmp_name'], 'uploads/' . $file['name']);
    }
}


?>