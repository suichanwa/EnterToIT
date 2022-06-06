<?php

require 'funcs.php';

$data = range(1, 100);

$per_page = 10;
$total = count($data);
$pages = ceil($total / $per_page);

$page = $_GET['page'] ?? 1;
$page = (int)$page;
if(!$page || $page < 1){
    $page = 1;
}
if($page > $pages){
    $page = $pages;
}

var_dump($page);

$start = ($page - 1) * $per_page;
var_dump($start);

debug(array_slice($data, $start, $per_page));

for($i = 0; $i <= $pages; $i++){
    echo "<a href='?page=$i'>$i</a>";
}



?>