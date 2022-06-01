<?php

header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');

include_once '../core/initializate.php';

$post = new Post($db);

$result = $post->read();

$num = $result->rowCount();


if($num > 0){
    $post_arr = array();
    $post_arr['data'] = array();

    while($row = $result -> fetch(PDO::FETCH_ASSOC)){
        extract($row);

        $post_item = array(
            'id'                => $id,
            'title'             => $title,
            'body'              => html_entity_decode($body),
            'author'            => $author,
            'category_id'       => $category_id,
            'category_name'     => $category_name
        );

        array_push($post_arr['data'], $post_item);
    }
} else{
    $post_arr = array(
        'message' => 'No Posts Found'
    );
}
?>
