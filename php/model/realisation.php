<?php
class Email implements IMessage {
    function send() {
        echo 'Sending email...';
    }
}

class Video implements extendIMessage {
    function send() {
        echo 'Sending video...';
    }

    function sendVideo() {
        echo 'Sending video...';
    }
}

class Mobile implements IMessage, iCamera {
    function send() {
        echo 'Sending mobile...';
    }

    function makeVideo() {
        echo 'Making video...';
    }
}

$email = new Email();
$email->send();
$video = new Video();
$video->sendVideo();


class Company{
     
    public $name;
    function __construct($name){ $this->name = $name; }
}

class PersonAge{
     
    public $name, $company;
    function __construct($name, $company)
    { 
        $this->name = $name; 
        $this->company = $company;
    }
}

$microsoft = new Company("Microsoft");
$tom = new PersonAge("Tom", $microsoft);


$bob = clone $tom;      
$bob->name = "Bob";
$bob->company->name = "Google";   
$bob->languages[0] = "french";
echo $tom->company->name; 


?>