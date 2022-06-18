<?php



if(isset($_POST['username']) && isset($_POST['userage'])){
    $username = $_POST['username'];
    $userage = $_POST['userage'];

    try{
        $db = new PDO('mysql:host=localhost;dbname=testfromsql', 'root', '');
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $db->exec("SET NAMES 'utf8'");
        //$sql = "INSERT INTO testfromsql.Users (name, age) VALUES ('$username', '$userage')";
        //$db->exec($sql);
    }
    catch(PDOException $e){
        echo $sql . "<br>" . $e->getMessage();
    }
}

if(isset($_POST['username']) && isset($_POST['userage'])){
    //echo 'User has been added successfully';
}



function print_r_html($data) {
    echo '<pre>';
    print_r($data);
    echo '</pre>';
}





$conn = new mysqli("localhost", "root", "", "users");
$sql = 'SELECT * FROM Users';

$result = mysqli_query($conn, $sql);
?>

<form method="GET" name="">
	<table>
		<tr>
			<td><input type="text" name="k" value="<?php echo isset($_GET['k']) ? $_GET['k'] : ''; ?>" placeholder="Enter your search keywords" /></td>
			<td><input type="submit" name="" value="Search" /></td>
		</tr>
	</table>
</form>



<?php
if (isset($_POST["username"]) && isset($_POST["userage"])) {
     
    try {
        $conn = new PDO("mysql:host=localhost;dbname=users", "root", "mypassword");
        $sql = "INSERT INTO Users (name, age) VALUES (:username, :userage)";
        $stmt = $conn->prepare($sql);
        $stmt->bindValue(":username", $_POST["username"]);
        $stmt->bindValue(":userage", $_POST["userage"]);
        $affectedRowsNumber = $stmt->execute();
        if($affectedRowsNumber > 0 ){
            echo "Data successfully added: name=" . $_POST["username"] ."  age= " . $_POST["userage"];  
        }

        $sql = "SELECT * FROM Users";
        $result = $conn->query($sql);



        echo "<table>";
        echo "<tr><th>ID</th><th>Name</th><th>Age</th></tr>";
        while($row = $result->fetch()) {
            echo "<tr><td>" . $row["id"] . "</td><td>" . $row["name"] . "</td><td>" . $row["age"] . "</td></tr>";
        }
    }
    catch (PDOException $e) {
        echo "Database error: " . $e->getMessage();
    }
}
?>






<form method="post">
    <p>User Name:
    <input type="text" name="username" /></p>
    <p>User Age:
    <input type="number" name="userage" /></p>
    <input type="submit" value="Save">
</form>


