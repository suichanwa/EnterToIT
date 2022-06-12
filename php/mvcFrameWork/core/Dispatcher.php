<?php
namespace core;

class Dispatcher{
    public function getPage(Track $track){
        $controller = $track->controller;
        $action = $track->action;
        $params = $track->params;
        
        $controller = new $controller();
        $controller->$action($params);
        
        //return controller and render it
        return $controller->render();
    }
}



?>