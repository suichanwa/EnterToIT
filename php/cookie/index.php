<?php

echo "<form action='index.php' method='post'>";
echo "<input type='text' name='name' placeholder='Enter your name'>";
echo "<input type='submit' name='submit' value='Submit'>";
echo "</form>";

?>

<?php
    $cookie_name = "user";
    $cookie_value = $_POST["username"];
    setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
    setcookie('username', '');

    $_COOKIE['username'] = '';


    //check if user have already been on site and if cookie is set
    if(isset($_COOKIE['username'])){
        echo 'Welcome back ' . $_COOKIE['username'];
    }else{
        echo 'Welcome to our site';
    }


?>