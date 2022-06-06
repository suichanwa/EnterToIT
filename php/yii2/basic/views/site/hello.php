<?php
namespace app\controllers;
use app\controllers\on;
use yii\base\Event;
use yii\base\BaseObject;


class Foo extends BaseObject{
    private $_lable;
    const EVENT_AFTER_SET_LABEL = 'afterSetLabel';

    public function getLable() {
        return $this->_lable;
    }

    public function setLable(){
        $this->_lable = "Hello World";
    }

    public function funcname($event){
        echo "Foo::" . $event->sender->getLable();
    }
}

$foo = new Foo;

$foo->on(Foo::EVENT_AFTER_SET_LABEL, function($event){
    echo "Foo::" . $event->sender->getLable();
});


?>