<?php

$db_user        = 'root';
$db_password    = '';
$db_name        = 'restfulapp';


$db = new PDO('mysql:host=localhost;dbname='.$db_name, $db_user, $db_password);
$db->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
$db->setAttribute(PDO::MYSQL_ATTR_USE_BUFFERED_QUERY, true);

$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

defined('APP_NAME', 'PHP RESTful API');

?>
