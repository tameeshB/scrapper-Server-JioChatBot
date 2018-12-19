<?php

$parts = parse_url($url);
parse_str($parts['query'], $param);

$query = $param['query'];
$min = '-1';
$max = '-1';
if(isset($param['min'])){
	$min = (string)$param['min'];
}else{
	$min = '-1'; 
}

if(isset($param['max'])){
	$max = (string)$param['max'];
}else{
	$max = '-1'; 
}

$temp = shell_exec('python3 flipkartParse.py '. $query .' '. $min .' '. $max);

echo $temp;
