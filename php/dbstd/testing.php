<?php

session_start();

$pdo = new PDO('mysql:host=localhost;dbname=users', 'root', '');

$sql = 'SELECT * FROM Users ORder BY name';

$q = $pdo->query($sql);

$q->setFetchMode(PDO::FETCH_ASSOC);

try {
    $pdo = new PDO('mysql:host=localhost;dbname=users', 'root', '');

    $sql = 'SELECT * FROM Users ORder BY name';

    $q = $pdo->query($sql);

    $q->setFetchMode(PDO::FETCH_ASSOC);
} catch(PDOException $e){
    echo $sql . "<br>" . $e->getMessage();
}

if(isset($_POST['username']) && isset($_POST['userage'])){
    try {
        $pdo = new PDO('mysql:host=localhost;dbname=users', 'root', '');

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

$rowsPerPage = 10;
$sql = 'SELECT * FROM Users';
$q = $pdo->query($sql);
$q->setFetchMode(PDO::FETCH_ASSOC);
$totalRows = $q->rowCount();
$totalPages = ceil($totalRows / $rowsPerPage);
$currentPage = isset($_GET['page']) ? $_GET['page'] : 1;
$offset = ($currentPage - 1) * $rowsPerPage;
$sql = 'SELECT * FROM Users LIMIT :offset, :rowsPerPage';
$stmt = $pdo->prepare($sql);
$stmt->bindValue(":offset", $offset, PDO::PARAM_INT);
$stmt->bindValue(":rowsPerPage", $rowsPerPage, PDO::PARAM_INT);
$stmt->execute();
$q = $stmt;
$q->setFetchMode(PDO::FETCH_ASSOC);

if(isset($_POST['search'])){
    $sql = 'SELECT * FROM Users WHERE name LIKE :search';
    $stmt = $pdo->prepare($sql);
    $stmt->bindValue(":search", '%' . $_POST['search'] . '%');
    $stmt->execute();
    $q = $stmt;
    $q->setFetchMode(PDO::FETCH_ASSOC);
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
    <?php for($i = 1; $i <= $totalPages; $i++): ?>
        <a href="?page=<?php echo $i; ?>"><?php echo $i; ?></a>
    <?php endfor; ?>
    <br>


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

    <form method="POST" action="">
        <table>
            <tr>
                <td>Search:</td>
                <td><input type="text" name="search" value="<?php echo isset($_POST['search']) ? $_POST['search'] : ''; ?>" placeholder="Enter your name" /></td>
            </tr>
            <tr>
                <td></td>
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