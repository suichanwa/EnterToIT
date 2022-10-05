<form action="index.php" method="post">
    <label for="username">Username:</label>
    <input type="text" name="username" id="username" />
    <label for="password">Password:</label>
    <input type="password" name="password" id="password" />
    <button type="submit" name="login" id="login" value="Login" />  
</form>


<form action="index.php" method="post">

</form>

<?php
session_start();

require 'database.php';
ini_set('display_errors', 1);

$conn = new PDO("mysql:host=$server;dbname=$db", $user, $pass);
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

if(!empty($_POST)){
    $username = filter_var($_POST['username'], FILTER_SANITIZE_STRING);
    $password = filter_var($_POST['password'], FILTER_SANITIZE_STRING);
    
    
    $stmt = $conn->prepare("SELECT * FROM students WHERE username = :username AND password = :password");
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $password);
    $stmt->execute();
    
    $result = $stmt->fetch(PDO::FETCH_ASSOC);
    
    if($result){
        echo 'You are logged in';
    } else {
        echo 'You are not logged in';
    }
}


$strSql = "SELECT * FROM students";
echo $strSql;
?>

