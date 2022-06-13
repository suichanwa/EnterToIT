<?php

//i've been study php 8.1 news features


interface I {
    public function foo();
}

interface ToString{
    public function __toString();
}

class userName implements ToString{
    public function __toString(){
        return "userName";
    }
}


class MainClass{
    public readonly string $user;
    

    public function __construct()  {
        $this->foo = 'bar';
    }
}

enum UserStatus: int implements I
{
    case Active = 1;
    case Inactive = 2;
    case Deleted = 3;

    public function text(){
        return match($this){
            self::Active => 'Active',
            self::Inactive => 'Inactive',
            self::Deleted => 'Deleted'
        };
    }

    public function value(){
        return match($this){
            self::Active => 1,
            self::Inactive => 2,
            self::Deleted => 3
        };
    }


    public static function StaticMethod(){
        return 'StaticMethod'; 
    }

    public function foo(){
        return 'foo';
    }
}


function main(){
    $user = UserStatus::Active;
    echo $user->text();
    echo $user->value();
    echo UserStatus::StaticMethod();
    echo $user->foo();
}

$numbers = [1,2,3,4,5, 'name' => 'userName'];

$s = array_is_list($numbers);
echo($s);


?>