<?php


include('model/intrefasce.php');
include('model/traits.php');
include('model/realisation.php');

class Oop {
    private $privateA = 'privateA';
    public $publicA = 'publicA';
    protected $protectedA = 'protectedA';

    private $sum = 0;

    protected function getProtectedMethod(){
        return 'protectedMethod';
    }

    public function getPublicMethod(){
        return 'publicMethod';
    }


    function testing(){
        echo $this->privateA;
        echo $this->publicA;
        echo $this->protectedA;
        echo $this->getProtectedMethod();
        echo $this->getPublicMethod();
    }

    function __construct($sum){
        $this->sum = $sum;
    }

    function getSum($firstAcc, $money){
        $firstAcc -> sum -= $money;
        $this -> sum += $money;
    }

    function printSum(){
        echo $this->sum;
    }

    //create a function that check if number is possitive
    function isPossitive($number){
        if($number > 0){
            return true;
        }
        return false;
    }

    function __destruct(){
        echo 'destructor';
    } 
}

function select($n): callable{
    switch($n){
        case 1: return function($a, $b) {return $a + $b;}; 
        case 2: return function($a, $b) {return $a - $b;};
        case 3: return function($a, $b) {return $a * $b;};
        default: return function($a, $b) {return $a . " " . $b;};
    }
}
$selection = select(2);
echo $selection(4,5);   // -1

class Node{
     
    function generate() : static{
        return new Node();
    }
}

$node1 = new Node();
$node2 = $node1->generate();


function AccSum(){
    $oop = new Oop(100);
    $oop->testing();
    $oop->getSum($oop, 50);
    $oop->printSum();
}
AccSum();

$person = new Person();
$person->name = 'John';
$person->age = 30;
print $person->name . ' is ' . $person->age . ' years old.';



class Person {
    public $name;
    public $age;
    static $count = 0;


    function __construct() {
        $this->name = 'another name';
        $this->age = 30;
    }

    function displayInfo2(){ 
        echo 'write something';
    
    }

    function __destruct() {
        echo 'Destructor called';
    }
}

final class Employee extends Person {
    public $salary;

    function __construct($name, $age, $salary) {
        parent::__construct($name, $age);
        $this->salary = $salary;
    }

    function displayInfo() {
        echo $this->name . ' is ' . $this->age . ' years old and earns ' . $this->salary . ' dollars a month.';
    }
}


$employee = new Employee('John', 30, 5000);
$employee->displayInfo();

class Users{
    public $name, $age;

    function __construct($name, $age){
        $this->name = $name;
        $this->age = $age;
    }
    function displayInfo($name, $age){
        echo 'Name:' . $this->name;
        echo 'Age:'  . $this->age;
    }

    function __destruct(){}
}




#$tomas = new Users('Tomas', '25');
#$tomas->displayInfo('Tomas', '25');


$pers = new class {
    public $name;
    public $age;

    function displayInfo(){
        echo 'Name: ' . $this->name;
        echo 'Age: ' . $this->age;
    }

    function __destructor(){}
}; 


class firstClass{
    public $name = 'John';
    public $age = 22222;
}

class classTwo{
    function displayInfo($name, $age){
        echo 'Name: ' . $name;
        echo 'Age: ' . $age;
    }
}

class Main{
    public function __construct(){
        $firstClass = new firstClass();
        $classTwo = new classTwo();
        $classTwo->displayInfo($firstClass->name, $firstClass->age);
    }
}

//$main = new Main();
//$main -> __construct();

class printText{
    use Printer;
}

$printex = new printText();
$printex->printText("\r\n helo from trait \r\n");

?>
