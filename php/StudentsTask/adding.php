<form action="adding.php">
    <div class="form-group">
        <label for="username">Username</label>
        <input type="text" class="form-control" name="username" id="username">
    </div
    
    <div>
        <label for="password">Password</label>
        <input type="password" class="form-control" name="password" id="password">
    </div>

    <input type="submit" class="btn btn-primary" name="submit" value="Submit">
</form>

<?php

$conn = new mysqli("localhost","root","root","students");

if ($conn->connect_error) {
    die("Connection failed: ". $conn->connect_error);
}

$name = $_REQUEST['username'];
$password = $_REQUEST['password'];


$sql = "INSERT INTO `students` (`username`, `password`) VALUES ('$name', '$password')";

$result = $conn->query($sql);

if ($result) {
    echo "<h1>User added successfully</h1>";
    echo "<p>Username: $name</p>";
    echo "<p>Password: $password</p>";
    echo "<p><a href='index.php'>Back to index</a></p>";
}

?>

