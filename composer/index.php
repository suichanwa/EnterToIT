<form action="user.php" method="POST">
    <input type="text" name="search" placeholder="Search...">
    <input type="submit" value="Search">
</form>



<?php

error_reporting(E_ALL);
ini_set('display_errors', 1);
mb_internal_encoding('UTF-8');


$name = "не определено";
$age = "не определен";
if(isset($_POST["name"])){
  
    $name = htmlentities($_POST["name"]);
}
if(isset($_POST["age"])){
  
    $age = htmlentities($_POST["age"]);
}
echo "Имя: $name <br> Возраст: $age";
?>