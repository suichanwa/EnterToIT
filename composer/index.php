<?php
include_once(__DIR__.'/vendor/autoload.php'); 

use Brick\Math\BigInteger;
use Brick\Math\BigDecimal;
echo BigInteger::of(2)->multipliedBy(BigDecimal::of('2.0')); // 4
echo BigInteger::of(2)->multipliedBy(BigDecimal::of('2.5')); // RoundingNecessaryException
echo BigDecimal::of(2.5)->multipliedBy(BigInteger::of(2)); // 5.0