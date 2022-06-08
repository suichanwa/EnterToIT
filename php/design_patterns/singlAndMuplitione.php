<?php


class Singleton{
    private static $instance = [];

    protected function __construct(){
        
    }

    protected function __clone(){
        
    }

    protected function __wakeup(){
        throw new \Exception('Deserializing is not allowed.');
    }

    public static function getInstance(string $instanceName){
        if(!isset(self::$instance[$instanceName])){
            self::$instance[$instanceName] = new self();
        } 
    }

    public function bussinesLogic(){
        //...
    } 
}

class Realization{
    public function clientCode(){
        $instance = Singleton::getInstance("somename");
    }
}

function clientCode(){
    $s1 = Singleton::getInstance("somename");
    $s2 = Singleton::getInstance("somename");

    if($s1 === $s2){
        echo "Singleton works, both variables contain the same instance.";
    } else {
        echo "Singleton failed, variables contain different instances.";
    }
    
}

?>