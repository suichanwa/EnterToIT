<?php
require_once('connect.php');
require_once('db.php');
session_start(); 

if($_SESSION['user']){
    header('location: index.php');
}

?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <form action="signin.php" method="post">
        <label>Логин</label>
        <input type="text" name="login" placeholder="Введите свой логин">
        <label>Пароль</label>
        <input type="password" name="password" placeholder="Введите пароль">
        <button type="submit">Войти</button>
        <p>
            У вас нет аккаунта? - <a href="register.php">зарегистрируйтесь</a>!
        </p>
        <?php
            // Проверяем наличие ошибок в форме
            if(isset($_SESSION['error'])){
                echo '<p style="color: red;">'.$_SESSION['error'].'</p>';
                unset($_SESSION['error']);
            }


            //[x] get all data from form
            if(isset($_POST['login'])){
                $login = $_POST['login'];
                $password = $_POST['password'];
            }      


            //[x] check if user entered correct data
            $query = "SELECT * FROM db_name WHERE login = '$login' AND password = '$password'";
            $result = mysqli_query($conn, $query);
            $user = mysqli_fetch_assoc($result);
            if($user){
                $_SESSION['user'] = $user;
                header('location: index.php');
            }else{
                echo '<p style="color: red;">Неверный логин или пароль</p>';
            }
        ?>
    </form>


</body>
</html>