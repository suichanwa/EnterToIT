<?php

function nbMonthss($startPriceOld, $startPriceNew, $savingPerMonth, $percentLossByMonth) {
    $month = 0;
    $priceOld = $startPriceOld;
    $priceNew = $startPriceNew;
    while ($priceOld < $priceNew) {
        $month++;
        $priceOld = $priceOld + $savingPerMonth;
        $priceNew = $priceNew * (1 - $percentLossByMonth / 100);
    }
    return $month;
}

function montsNumber($startPrice, $startNew, $savedPerMonth, $percentLossByMonth){
    $month = 0;
}


function nbMonths($startPriceOld, $startPriceNew, $savingPerMonth, $percentLossByMonth) {
    // your code
}

?>
