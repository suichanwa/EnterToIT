<?php
require 'database.php';


if($_POST['submit']){
    %key = $_POST['key'];
    $sql = "SELECT * FROM users WHERE username = '$key'";
}

?>



<form action="foo.php" method="post">
    <input type="text" name="foo" value="bar" />
    <input type="submit" value="Submit" />
</form>



<?php

ini_set('display_errors', 1);


class Student{
    public string $name = 'someName';
    public int $age  = 12;
}

$student = new Student();

if(isset($_POST['name'])){
    $student->name = $_POST['name'];
}



?>
