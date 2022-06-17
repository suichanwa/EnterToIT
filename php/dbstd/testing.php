<?php

session_start();

$pdo = new PDO('mysql:host=localhost;dbname=users', 'root', '', $name);

$sql = 'SELECT * FROM Users ORder BY name';

$q = $pdo->query($sql);

$q->setFetchMode(PDO::FETCH_ASSOC);

try {
    $pdo = new PDO('mysql:host=localhost;dbname=users', 'root', '', $name );

    $sql = 'SELECT * FROM Users ORder BY name';

    $q = $pdo->query($sql);

    $q->setFetchMode(PDO::FETCH_ASSOC);
} catch(PDOException $e){
    echo $sql . "<br>" . $e->getMessage();
}

if(isset($_GET['k'])){
    $k = $_GET['k'];
    $sql = "SELECT * FROM Users WHERE name LIKE '%$k%'";
    $q = $pdo->query($sql);
    $q->setFetchMode(PDO::FETCH_ASSOC);
}

//create a logic to adding a new user to database
if(isset($_POST['username']) && isset($_POST['userage'])){
    try {
        $pdo = new PDO('mysql:host=localhost;dbname=users', 'root', '', $name );

        $sql = 'INSERT INTO Users (name, age) VALUES (:username, :userage)';

        $stmt = $pdo->prepare($sql);
        $stmt->bindValue(":username", $_POST["username"]);
        $stmt->bindValue(":userage", $_POST["userage"]);
        $affectedRowsNumber = $stmt->execute();
        if($affectedRowsNumber > 0 ){
            echo "Data successfully added: name=" . $_POST["username"] ."  age= " . $_POST["userage"];  
        }
    } catch(PDOException $e){
        echo $sql . "<br>" . $e->getMessage();
    }
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
    <form method="POST" action="">
        <table>
            <tr>
                <td>Name:</td>
                <td><input type="text" name="username" value="<?php echo isset($_POST['username']) ? $_POST['username'] : ''; ?>" placeholder="Enter your name" /></td>
            </tr>
            <tr>
                <td>Age:</td>
                <td><input type="text" name="userage" value="<?php echo isset($_POST['userage']) ? $_POST['userage'] : ''; ?>" placeholder="Enter your age" /></td>
            </tr>
            <tr>
                <td></td>
                <td><input type="submit" name="" value="Add" /></td>
            </tr>
        </table>
    </form>

    <form method="GET" name="">
        <table>
            <tr>
                <td><input type="text" name="k" value="<?php echo isset($_GET['k']) ? $_GET['k'] : ''; ?>" placeholder="Enter your search keywords" /></td>
                <td><input type="submit" name="" value="Search" /></td>
            </tr>
        </table>
    </form>

    <div id="container">
        <h1>user info</h1>

        <table>
            <tr>
                <th>name</th>
                <th>age</th>
            </tr>
            <?php while ($row = $q->fetch()): ?>
                <tr>
                    <td><?php echo $row['name']; ?></td>
                    <td><?php echo $row['age']; ?></td>
                </tr>
            <?php endwhile; ?>
    </div> 
</body>
</html>