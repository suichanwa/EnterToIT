<?php

namespace base;

class SomeClass
{
    private $param1;
    private $param2;


    public function doSomething()
    {
        echo 'doSomething';
    }
}

$someClass = new SomeClass();
$someClass->doSomething();

?>
