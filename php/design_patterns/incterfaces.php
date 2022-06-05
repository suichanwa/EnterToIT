<?php
interface WriteFactory{
    public function createCvsWriteer();
    public function createJsonWriteer();
}

interface CsvWritter{
  public function write(array $line): string;
}

interface JsonWritter{
  public function write(array $data, bool $formated): string;
}


trait MultionTrait{
  private static $list = [];

  public static function getInstance(string $instanceName): self{
    $class = get_called_class();
    if(!isset(self::$list[$class])){
      self::$list[$class] = new $class();
    }
    return self::$list[$class];
  }

  public function __constructor(){} 

  public function __clone(){
    trigger_error('Clone is not allowed.', E_USER_ERROR);
  }

  public function __wakeup(){
    trigger_error('Deserializing is not allowed.', E_USER_ERROR);
  } 
}


class foo{
  use MultionTrait;

  private $var = [];

  public function addvalue($value){
    $this->var[] = $value;
  }
    
  public function getvalue(){
    return $this->var;
  }
}


$foo1 = foo::getInstance('somename');

$foo1->addvalue('foo');
$foo1->addvalue('bar');

$pr = $foo1->getvalue();

print_r($pr);

?>