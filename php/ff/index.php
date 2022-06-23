<?php

require_once 'vendor/autoload.php';

$f3 = Base::instance();

//create a route using f3 framework
$f3->route('GET /', function() {
    echo '<h1>Hello World</h1>';
});

$f3->route('GET /@name', function($f3, $params) {
    echo '<h1>Hello ' . $params['name'] . '</h1>';
});


$f3->set('DB', new DB\SQL(
    'mysql:host=localhost;port=3306;dbname=f3_db',
    'root',
    ''
));

//create a table to mysql with user that will have name, id and score
$f3->get('/create_table', function() {
    $db = $f3->get('DB');
    $db->exec('CREATE TABLE users (name VARCHAR(255), id INT, score INT)');
});



$f3->run();

?>
