<?php
interface IMessage 
{
    function send();
}

interface extendIMessage extends IMessage 
{
    function sendVideo();
}


interface iCamera
{
    function makeVideo() ;
}

abstract class Messanger 
{
    protected $name;
    abstract function sendSomething($message);

    function __construct($name){
        $this->name = $name;
    }

    function close(){
        echo 'Closing...';
    }
}

class EmailSs extends Messanger {
    function sendSomething($message){
        echo 'Sending email...';
    }
}

$email = new EmailSs('John');
$email->sendSomething('Hello');
$email->close();

?>