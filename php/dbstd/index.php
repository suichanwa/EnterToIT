<form method="post">
    <p>User Name:
    <input type="text" name="username" /></p>
    <p>User Age:
    <input type="number" name="userage" /></p>
    <input type="submit" value="Save">
</form>


<?php


$conn = new mysqli("localhost", "root", "", "testfromsql");
$sql = 'SELECT * FROM testfromsql';

$result = mysqli_query($conn, $sql);

while($row = mysqli_fetch_assoc($result)){
    echo $row['name'] . ' ' . $row['age'] . '<br>';
}




if(isset($_POST['username']) && isset($_POST['userage'])){
    $username = $_POST['username'];
    $userage = $_POST['userage'];

    try{
        $db = new PDO('mysql:host=localhost;dbname=testfromsql', 'root', '');
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $db->exec("SET NAMES 'utf8'");
        $sql = "INSERT INTO testfromsql.Users (name, age) VALUES ('$username', '$userage')";
        $db->exec($sql);
    }
    catch(PDOException $e){
        echo $sql . "<br>" . $e->getMessage();
    }
}

//if user have been added successfully, show message
if(isset($_POST['username']) && isset($_POST['userage'])){
    echo 'User has been added successfully';
}



function print_r_html($data) {
    echo '<pre>';
    print_r($data);
    echo '</pre>';
}



try {
    $conn = new PDO("mysql:host=localhost;dbname=testfromsql", "root", "", );
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    //$sql = "CREATE DATABASE IF NOT EXISTS `testfromsql`";
    /*$sql = "CREATE TABLE IF NOT EXISTS `testfromsql` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `name` varchar(255) NOT NULL,
        `email` varchar(255) NOT NULL,
        `password` varchar(255) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8";
    */
    //$sql = "INSERT INTO testfromsql (name, email, password) VALUES ('John', 'email@com.test', 'password')";

    //$conn->exec($sql);

    print_r_html("Database created successfully");
}
catch(PDOException $e){
    echo "Connection failed: " . $e->getMessage();
}

?>