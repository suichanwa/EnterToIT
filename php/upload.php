<?php


$arr = [];
for($a = 0; $a < 10; $a++){
    for($j = 0; $j < 10; $j++){
        $arr[$a][$j] = rand(0, 100);
    }
}

print($arr);
?>