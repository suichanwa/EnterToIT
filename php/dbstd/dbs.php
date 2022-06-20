<?php

$dbname = "users";

try {
    $conn = new PDO("mysql:host=localhost;dbname=$dbname", "root", "");
    $sql = "UPDATE Users SET AGE = :age WHERE ID = :id";
    $affected_rows = $conn->prepare($sql)->execute(array(
        ':age' => '25',
        ':id' => '1'
    ));
    echo "Affected rows: $affected_rows";
} 
catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

class InserData{
    const DB_NAME = "users";
    const DB_USER = "root";
    const DB_PASS = "";
    const DB_HOST = "localhost";

    public function __construct(){
        $conStr = sprintf("mysql:host=%s;dbname=%s", self::DB_HOST, self::DB_NAME);

        try{
            $this->conn = new PDO($conStr, self::DB_USER, self::DB_PASS);
        } catch(PDOException $e){
            echo "Connection failed: " . $e->getMessage();
        }
    }
    
    public function insert(){
        $sql = "INSERT INTO Users (NAME, AGE) VALUES ('John', '25')";
        $affected_rows = $this->conn->exec($sql);
        echo "Affected rows: $affected_rows";

    }

    
    function insertSingleRow($subject, $deskription, $startData, $endData, $userId){
        $sql = "INSERT INTO Events (subject, deskription, startData, endData, userId) VALUES ('$subject', '$deskription', '$startData', '$endData', '$userId')";
        echo "Affected rows: $affected_rows";
    }


     public function update($id, $subject, $description, $startDate, $endDate) {
        $task = [
            ':taskid' => $id,
            ':subject' => $subject,
            ':description' => $description,
            ':start_date' => $startDate,
            ':end_date' => $endDate];


        $sql = 'UPDATE tasks
                    SET subject      = :subject,
                         start_date  = :start_date,
                         end_date    = :end_date,
                         description = :description
                  WHERE task_id = :taskid';

        $q = $this->pdo->prepare($sql);

        return $q->execute($task);
    }

    function __destruct(){
        $this->conn = null;
    }
}

$insertD = new InserData();


?>
