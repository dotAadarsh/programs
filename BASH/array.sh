#!/bin/bash

# Declaring an array
declare -a example_array=( "Theres" "nothing" "holding" "me" "back" )

echo ${example_array[2]}
echo "${!example_array[@]}" # Printing the keys
echo "The array contains ${#example_array[@]} elements" #finding len 

#loop through array

for i in "${!example_array[@]}"
do 
echo "The key value of the element "${example_array[$i]}" is $i"
done