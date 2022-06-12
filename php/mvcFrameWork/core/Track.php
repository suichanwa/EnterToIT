<?php

namespace core;

class Track{
    private $controller;
    private $action;
    private $params;
    
    public function __construct($controller, $action, $params){
        $this->controller = $controller;
        $this->action = $action;
        $this->params = $params;
    }

    public function __get($property){
        return $this->$property;
    }

    public function getTrack($routes, $uri){

        foreach ($routes as $route){
            if($route->path == $uri){
                $this->controller = $route->controller;
                $this->action = $route->action;
                $this->params = $route->params;
                return true;
            }
        }

        return static::getTrack($routes, '404');
    }
}

?>