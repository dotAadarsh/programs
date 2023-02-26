#1/bin/bash

echo "Do you know bash programming"
read -p "Yes/No?" answer

case $answer in 
    Yes|yes|Y|y)
        echo "Thats amazing"
        echo
        ;;
    No|no|n|N)
        echo "Its easy tho..."
        ;;
esac