#!/bin/bash
# Basic example of for loop

greeting="Hello there"

for word in $greeting
do 
echo $word
done

echo "Thank you!"

for num in {1..10}
do
echo $num
done

echo "Series of numbers from 1 to 10"

for num in {1..10..2}
do 
echo $num
done
echo "Increment each by 2"
echo


echo "for loop to read array var"

arr=( "This""is""an""array" )
for i in "${arr[@]}"
do 
echo $i
done

string="this is a string"
for i in $string
do
echo $i
done

for ((i=1;i<=10;i++))
do
echo "$i"
done

for ((i=1;i<=10;i++))
do
echo "$i"
if [ $i == 7 ];
then
break
fi
done