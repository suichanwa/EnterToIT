<?php
    $arr = [];

    for($a = 0; $a < 1; $a++){
        for($j = 0; $j < 1; $j++){
            $arr[$a][$j] = rand(0, 10);
        }
    }

    echo json_encode($arr);

    $products = [
		[
			'name'   => 'мясо',
			'price'  => 100,
			'amount' => 5,
		],
		[
			'name'   => 'овощи',
			'price'  => 200,
			'amount' => 6,
		],
		[
			'name'   => 'фрукты',
			'price'  => 300,
			'amount' => 7,
		],
	];
    
    foreach($products as $product){
        echo $product['name'] . " " . $product['price'] . " " . $product['amount'];
    }


    $arr = ['a', 'b', 'c', 'd', 'e'];

   $result = array_slice($arr, 2, 2); 
    foreach($result as $item){
       echo $item . " ";
    }

?>