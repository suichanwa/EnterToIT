<?php

$name = "не определено";
$age = "не определен";
if(isset($_POST["name"])){
  
    $name = htmlentities($_POST["name"]);
}
if(isset($_POST["age"])){
  
    $age = htmlentities($_POST["age"]);
}
echo "Имя: $name <br> Возраст: $age";

