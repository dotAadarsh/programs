#!/bin/bash
#Example for bash split string by space

read -p "Enter any string by space: " str # reading string value

IFS="" #setting space as delimiter
read
ra ADDR <<<"$str" # reading str as array as token separated by IFS

for i in "${ADDR[@]}"; # Accessing each element of array
do
echo "$i"
done