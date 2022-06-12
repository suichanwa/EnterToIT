<?php

namespace core;
use core\Track;

class Route{
    private $path;
    private $controller;
    private $action;

    public function __construct($path, $controller, $action){
        $this->path = $path;
        $this->controller = $controller;
        $this->action = $action;
    } 

    public function __get($path){
        return $this->$path;
    }

    public function getTrack(){
        $track = new Track($this->controller, $this->action, $this->params);
        return $track; 
    }
}


?>
