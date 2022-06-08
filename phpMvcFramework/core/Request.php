<?php
namespace app\core;

/**
 * @author suichanwa
 * @package app\core
 * 
 */

 class Request{
    public function getPath(){
        $path = $_SERVER['REQUEST_URI'] ?? '/'; 
        $possition = strpos($path, '?');

        if($possition !== false){
            $path = substr($path, 0, $possition);
        }
    }

    public function getMethod(){
        $path = $_SERVER['REQUEST_METHOD'] ?? 'GET';
        $position = strpos($path, '?');

        if($position === false){
            return $path;
        }

        return substr($path, 0, $position);
    }

    public function get($key){
         return $_GET[$key];
     }
 }

?>