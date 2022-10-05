<?php
$server = 'localhost';
$user = 'root';
$pass = 'root';
$db = 'students';

$conn = new mysqli($server,$user,$pass,$db);

$sql = 'create table students(
    username varchar(255) not null
    password varchar(255) not null
)';

if($conn->connect_errno){
    die('Connection failed: '. $conn->connect_error);
}



if($conn->query($sql) === TRUE){
    echo 'all have benn done';
} else {
    echo 'all have not benn done';
}


$conn->close();
?>