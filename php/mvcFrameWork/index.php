<?php
include('core/Route.php');
use core\Route;

error_reporting(E_ALL);
ini_set('display_errors', 1);

function my_autoloader($class){
    $class = str_replace('\\', '/', $class);
    $file = 'core/' . $class . '.php';
    if(file_exists($file)){
        require_once $file;
    }
}

spl_autoload_register(function ($class) {
    $path = __DIR__ . $class . '.php';
    if (file_exists($path)) {
        require_once $path;
    }
});




$track = (new Route('/', 'home', 'index'))->__get('path');



?>

