<?php
namespace core;

class Controler{
    protected function render($view, $data = []){
        return new Page('layout.php', 'My MVC', $view, $data);
    }
}


?>