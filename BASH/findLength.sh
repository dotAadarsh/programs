#!bin/bash
# bash program to find the length of the string

string1="Length of the string"
len=${#string1}

echo "Length of $string1 is $len"

string2="this is for expr"
length=`expr length "$string2"`
echo "Length of $string2 is $length"