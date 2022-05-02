#!/bin/bash

if [ $1 == "-h" ]; then
    printf "You can enter the name of a package to install it\nexample: ./helper.sh -i package\n"

elif [ $1 == "-i" ]; then
    git clone https://aur.archlinux.org/$2.git
    cd $2
    makepkg -si
fi

