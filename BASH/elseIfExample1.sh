#!/bin/bash

read -p "Enter the number of quantity: " num

if [ $num -gt 100 ];
then 
echo "Eligible for 10% discount"
elif [ $num -lt 100 ];
then
echo "Eligible for 5% discount"
else 
echo "Lucky draw winner"
echo "Eligible to get item for free"
fi
