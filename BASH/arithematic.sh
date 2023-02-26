#!/bin/bash  

# Double Parentheses
# Method 1
Sum=$((10+3))
echo "Sum = $Sum"

# Method 2
((Sum=10+3))
echo "Sum = $Sum"

# Method 3
Num1=10
Num2=3
((Sum=Num1+Num2))
echo "Sum = $Sum"

# Method 4 
Num1=10
Num2=3
Sum=$((Num1+Num2))
echo "Sum = $Sum"

# Operations
x=10
y=5
echo "x=$x and y=$y"
echo "Addition of x & y: $(($x+$y))"
echo "Subtraction of x & y: $(($x-$y))"
echo "Multiplication of x & y: $(($x*$y))"
echo "Division of x & y: $(($x/$y))"
# echo "Exponentiation of x & y: $(($x ** $y))" Throws error need to figure it out
echo "Modular division of x & y: $(($x%$y))"
echo "Incrementing y by 5, then y = $((y+=5))"
echo "Decrementing x by 5, then x = $((x-=5))"
echo "Multiplying x by 3, then x = $((x*=3))"
echo "Dividing y by 2, then y = $((y/=2))"
echo "Remainder of dividing x by 2, x = $((x%2))"