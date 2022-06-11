<?php

namespace core;


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
}


?>
