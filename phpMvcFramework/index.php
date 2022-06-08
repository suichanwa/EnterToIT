<?php

require_once __DIR__ . '/vendor/autoload.php';

use app\core\Application;
use app\core\Request;

/**
* @author suichanwa
* @package app\core 
*/

$app = new Application();

$app->router->get('/', function(){
    return 'Hello World!';
});

$app->router->get('/contact', function(){
    return 'Contact us!';
});

$app->run();


$app->router->resolve();



?>
