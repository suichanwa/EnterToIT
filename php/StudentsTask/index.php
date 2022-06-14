<?php
require 'database.php';




if($_POST['submit']){
    $key = $_POST['key'];
    $query = $pdo->prepare("SELECT * FROM students WHERE username LIKE '%$key%'");
    $query->bindValue(':key', $key, PDO::PARAM_STR);
    $query->execute();
    $result = $query->fetchAll();
    $rows = $query->rowCount();
}

?>



<form action="foo.php" method="post">
    <input type="text" name="foo" value="bar" />
    <input type="submit" value="Submit" />
</form>


<div>
    <?php
    if($rows > 0){
        foreach($result as $row){
            echo $row['username'] . '<br>';
        }
    }
    ?>
</div>


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
