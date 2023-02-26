#!/bin/bash
# script to get specified number

read -p "Enter the starting number" snum
read -p "Enter the ending number" enum

while [[ $snum -le $enum ]];
do 
echo $snum
((snum++))
done


echo "Upcoming is use of continue"

i=0
while [ $i -le 10 ]
do
((i++))
if [[ "$i" == 5 ]];
then 
    continue
fi
echo "Current number: $i"
done

echo "Skipped number 5"