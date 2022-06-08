<?php
namespace app\core;


/**
*@author suichanwa
*@package app\core 
*/

class Router{
    public Request $request;
    protected array $routes = [];

    public function __construct(\app\core\Request $request){
        $this->request = new Request();
    }

    public function get($path, $callback){
        $this->routes['GET'][$path] = $callback;
    }    

    public function resolve() {
        $path = $this->request->getPath();
        $this->request = new Request();
        $method = $this->request->getMethod();
        $callback = $this->routes[$method][$path];

        if($callback === false){
            echo "404";
        }

        echo call_user_func($callback);
   }
}

?>