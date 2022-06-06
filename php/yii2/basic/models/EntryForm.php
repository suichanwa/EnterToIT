<?php
namespace app\models;

use yii\base\Model;

class EntryForm extends Model{
    public $name;
    public $emial;

    public function rules(){
        return [
            [['name', 'email'], 'required'],
            ['email', 'email'],
        ];
    }

}

?>