<?php
include ('incterfaces.php');
session_start();

class UnixCsvWriteer implements CsvWritter{
  public function write(array $line): string{
    return implode(',', $line);
  }
}

class JsonWrite implements JsonWritter{
  public function write(array $data, bool $formated): string{
    if($formated){
      return json_encode($data, JSON_PRETTY_PRINT);
    }
    return json_encode($data);
  }
}

class UnixWriteFactory implements WriteFactory{
  public function createCvsWriteer(): CsvWritter{
    return new UnixCsvWriteer();
  }
  public function createJsonWriteer(): JsonWritter{
    return new JsonWritter();
  }
}


//example of factory pattern

class SomeObj{
  private $firstFild;
  private $secondFild;

  public function __construct($firstParam, $secondParam){
    $this->firstFild = $firstParam;
    $this->secondFild = $secondParam;
  }

  public function getName(): string{
    return $this->firstFild . ' ' . $this->secondFild;
  }
}


class ObjFactory{
  public static function createObj($firstParam, $secondParam): SomeObj{
    return new SomeObj($firstParam, $secondParam);
  }
}

$objName = new SomeObj('obj_name', 'second');
print_r($objName->getName());

?>