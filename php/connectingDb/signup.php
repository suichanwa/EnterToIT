<?php
    $first = $_POST['first'];
    $second = $_POST['second'];
    $submit = $_POST['submit'];



    include_once('db.php');

    $sql = "CREATE TABLE users {
        user_id int(11) AUTO_INCREMENT PRIMARY KEY not null,
        username varchar(255) not null,
        password varchar(255) not null,
        email varchar(255) not null,
    };

    INSERT INTO users (username, password, email) VALUES ('$first', '$second');
    ";

    header("Location: index.php");

?>