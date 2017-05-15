<?php 

echo "string";

$port = "80";

$data = system("parser.py 8.8.8.8 8.8.8.9 80");

var_dump($data);













?>