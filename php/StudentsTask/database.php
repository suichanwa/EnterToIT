<?php
$server = 'localhost';
$user = 'root';
$pass = '';
$db = 'students';


$conn = new mysqli($server, $user, $pass, $db);
if($conn->connect_error){
    die('Connection failed: ' . $conn->connect_error);
} else {
    echo 'Connected successfully'; 
}


try{
    $conn = new PDO("mysql:host=$server;dbname=$db", $user, $pass);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully " . $db;
}
catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
}

