<?php

require_once 'vendor/autoload.php';


$f3 = Base::instance();

$f3->route('GET /', function() {
    
});

$f3->set('DB', new DB\SQL(
    'mysql:host=localhost;port=3306;dbname=f3_db',
    'root',
    ''
));

$f3->run();
?>


<!DOCTYPE html>
<html>
    <head>
        <title>My Webpage</title>
    </head>
    <body>
        <ul id="navigation">
        {% for item in navigation %}
            <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
        {% endfor %}
        </ul>

        <h1>My Webpage</h1>
        {{ a_variable }}
    </body>
</html>