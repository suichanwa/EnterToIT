<?php

require __DIR__ . '/vendor/autoload.php';
require __DIR__ . '/vendor/fzaninotto/faker/src/autoload.php';

include "namespaces.php";

use base;
use GuzzleHttp\Psr7;
use GuzzleHttp\Client;
use Intervention\Image\ImageManager;
use SebastianBergmann\Timer\Timer;

$manager = new ImageManager(array('driver' => 'imagick'));
$faker = Faker\Factory::create();

$timer = new Timer;

$timer->start();

foreach(\range(0,1000) as $i) {
    $i *= $i;
}

$duration = $timer->stop();

var_dump(get_class($duration));
var_dump($duration->asString());

//$image = $manager->make('images/test.jpg')->resize(100, 100);

echo $faker->name;



$client = new Client([
    'base_uri' => 'http://httpbin.org',
    'timeout'  => 2.0,
]);

$SomeClass = new SomeClass();
$SomeClass->someMethod();


?>
