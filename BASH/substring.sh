#!/bin/bash
#scrip to extract first 10 characters of a string

echo "String: vandhaarai vaazha veikum chennai"
str="vandhaarai vaazha veikum chennai"

echo "total characters in a string: ${#str}"

substr="${str:0:10}"
echo "Substring: $substr"
echo "Total characters in substring ${#substr}"