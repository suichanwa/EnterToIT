<?php
trait Cemar {
    public function makeVideo() {
        echo 'Making video...';
    }
    public function doSome() {}
}

trait Printer{ 
    public function printText($text){
        echo "\r\n $text";
    }
}

?>