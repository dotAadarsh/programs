#!/bin/bash
# Let is a built-in command of Bash that allows us to perform arithmetic operations.

x=10
y=6
z=0
echo "Addition"
let "z = $((x+y))"
echo "z=$z"

# Simlar for other operators 