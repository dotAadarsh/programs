#!/bin/bash

# Method 1
print() {
    echo "Function is called"
}
print

# Method 2
function print2 {
    echo "This is using function keyword"
}
print2

# To pass and access arguments

function_arguments() {
    echo $1
    echo $2
    echo $3
    echo $4
}

function_arguments "Wubba""lubba""dub""dub"

#Variable scope
v1='A'
v2='B'

my_var() {
    local v1='C'
    v2='D'
    echo "Inside function"
    echo "v1 is $v1"
    echo "v2 is $v2"
}
echo "Before executing the function"
echo "v1 is $v1"
echo "v2 is $v2"

my_var

echo "Before executing the function"
echo "v1 is $v1"
echo "v2 is $v2"