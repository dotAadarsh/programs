#!/bin/bash
# Script to check whether two strings are equal

str1="Thisisbash"
str2="bash"

if [ $str1 = $str2 ];
then 
echo "Both strings are equal"
else
echo "String are not equal"
fi

if [ $str1 \> $str2 ];
then
    echo "$str1 is greater then $str2"  
else  
    echo "$str1 is less then $str2"  
fi  