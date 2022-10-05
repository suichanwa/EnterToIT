<?php
$server = 'localhost';
$user = 'root';
$pass = 'root';
$db = 'students';


function connection_db() {
    global $server, $user, $pass, $db;
    $conn = new PDO("mysql:host=$server;dbname=$db", $user, $pass);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    return $conn;
}

$conn = connection_db();

$conn->exec('SET NAMES utf8');

