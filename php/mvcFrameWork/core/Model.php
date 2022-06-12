<?php
namespace core;

class Model{
    private static $link;

    public function __construct(){
        $this->link = mysqli_connect('localhost', 'root', '', 'mvc');
        mysqli_query($this->link, "SET NAMES 'utf8'");
    }

    protected function findOne($query){
        $result = mysqli_query($this->link, $query);
        $row = mysqli_fetch_assoc($result);
        return $row;
    }

    protected function findAll($query){
        $result = mysqli_query($this->link, $query);
        $rows = [];
        while($row = mysqli_fetch_assoc($result)){
            $rows[] = $row;
        }
        return $rows;
    }
}



?>