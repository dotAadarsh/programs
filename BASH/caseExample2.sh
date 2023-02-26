#!/bin/bash

echo "Which OS are you using?"
echo "Windows, Androd, Chrome, Linux, Others?"
read -p "Type of OS name:" OS

case $OS in 
    Windows|windows)
        echo "Thats common. You should try something new!"
        echo
        ;;
    Android|android)
        echo "Lots of app yo"
        echo
        ;;
    Chrome|chrome)
        echo "Noice choice"
        echo 
        ;;
    Linux|linux)
        echo "You are a pro"
        echo
        ;;
    *)
        echo "Interesting. I will give it a try!"
        echo
        ;;
esac