#!/bin/bash

# Arithematic operations can also be performed using the backticks and expr 

echo "a=10, b=3"
echo "c is the value of addition c=a+b"
a=10
b=3
echo "c=`expr $a + $b`"