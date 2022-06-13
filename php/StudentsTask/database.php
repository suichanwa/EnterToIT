<?php
$server = 'localhost';
$user = 'root';
$pass = '';
$db = 'students';

try{
    $conn = new PDO("mysql:host=$server;dbname=$db", $user, $pass);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully" . $db;
}
catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
}

